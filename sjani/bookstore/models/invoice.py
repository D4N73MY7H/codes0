from datetime import datetime, timedelta

from odoo import models, fields, api
from odoo.exceptions import UserError


class Invoice(models.Model):
    _name = 'bookstore.invoice'
    _description = 'Invoice'
    _rec_name = 'invoice_number'

    invoice_number = fields.Char(
        default=lambda self: self.env['ir.sequence'].next_by_code('bookstore.invoice.sequence'))
    date = fields.Datetime(string='Date', required=True, default=lambda self: fields.Datetime.now())
    invoice_type = fields.Selection(string='Type', required=True,
                                    selection=[('in', 'Purchase'),
                                               ('out', 'Sale')])
    invoice_line_ids = fields.One2many(comodel_name='bookstore.invoice.line', inverse_name='invoice_id',
                                       string='Invoice Lines')
    total = fields.Float(string='Total', store=True, compute="_calc_total_invoice")
    reference_record = fields.Reference([('bookstore.book', 'Book')], string="Record")
    employee_id = fields.Many2one('bookstore.employee', string='Employee')

    # daily_turnover = fields.Float(string='Daily turnover', compute='check_daily_turnover')

    # @api.onchange('invoice_line_ids')
    # def _onchange_invoice_line_ids(self):
    #     for line in self.invoice_line_ids:
    #         self.reference_record = line.book_id
    #

    @api.depends('invoice_line_ids')
    def _calc_total_invoice(self):
        for invoice in self:
            invoice.total = sum(invoice.invoice_line_ids.mapped('total'))

    def confirm(self):

        if self.invoice_type == 'in':
            for invoice_line in self.invoice_line_ids:
                invoice_line.book_id.quantity_in_stock += invoice_line.quantity
        else:
            for invoice_line in self.invoice_line_ids:
                invoice_line.book_id.quantity_in_stock -= invoice_line.quantity

    # @api.model
    def check_daily_turnover(self):
        today = fields.Datetime.now().date()
        # employees = self.env['bookstore.employee'].search([])
        start_date = today
        end_date = today + timedelta(days=1)

        sales = self.env['bookstore.invoice'].read_group([
            ('date', '>=', start_date),
            ('date', '<', end_date),
        ], ['total:sum', 'employee_id.name'], ['employee_id'])

        emp_list = [{'employee': sale['employee_id'][1], 'daily_turnover': sale['total']} for sale in sales]

        # for employee in employees:
        #     sales = self.env['bookstore.invoice'].search([
        #         ('employee_id', '=', employee.id),
        #         ('date', '>=', start_date),
        #         ('date', '<', end_date),
        #     ])
        #     daily_turnover = sum(sales.mapped('total'))
        #     emp_list.append({'employee': employee.name, 'daily_turnover': daily_turnover})
        #     print(f"Employee {employee.name} has a daily turnover of {daily_turnover}")

        template = self.env.ref('bookstore.daily_turnover_mail_template')
        template.with_context({'daily_turnover': emp_list}).send_mail(self.search([], limit=1).id)

    def action_send_turnover_mail(self):
        template = self.env.ref('bookstore.daily_turnover_mail_template')
        for rec in self:
            template.send_mail(rec.id)

    # @api.model
    # def check_daily_turnover(self):
    #     today = datetime.now().date()
    #     employees = self.env['bookstore.employee'].search([])
    #     print(employees)
    #     for employee in employees:
    #         sales = self.env['bookstore.invoice'].search([('employee_id', '=', employee.id), ('date', '=', today)])
    #         print(employee, sales['total'])
    # daily_turnover = sum(sales.mapped('total'))
    # print(sales)
    # print(employee.id, employee.name, daily_turnover, datetime.now())


class InvoiceLine(models.Model):
    _name = 'bookstore.invoice.line'
    _description = 'InvoiceLine'

    quantity = fields.Float(string='Quantity', required=True)
    price = fields.Float(string='Price', required=True)
    book_id = fields.Many2one(comodel_name='bookstore.book', string='Book', required=True)
    invoice_id = fields.Many2one(comodel_name='bookstore.invoice', string='Invoice', required=True, ondelete="cascade")
    total = fields.Float(string='Total', compute="_calc_total")
    date = fields.Datetime(related='invoice_id.date', string="date")
    employee_id = fields.Many2one('bookstore.employee', string='Employee')

    @api.onchange('book_id')
    def onchange_product_id(self):
        if self.invoice_id.invoice_type == 'in':
            self.price = self.book_id.purchase_price
        else:
            self.price = self.book_id.sale_price

    @api.depends('quantity', 'price')
    def _calc_total(self):
        for invoice_line in self:
            invoice_line.total = invoice_line.quantity * invoice_line.price

    # def check_daily_turnover(self):
    #     today = fields.Date.today()
    #     invice = self.env['bookstore.invoice'].search([('date', '=', today)])

    # @api.model
    # def create(self, values):
    #     record = super(bookstore.InvoiceLine, self).create(values)
    #     if record.quantity_in_stock < record.min_quantity:
    #         raise UserError("Kujdes!")
    #     return record
