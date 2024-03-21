from odoo import models, fields, api
from odoo.exceptions import UserError


class Invoice(models.Model):
    _name = 'bookstore.invoice'
    _description = 'Invoice'
    _rec_name = 'invoice_number'

    invoice_number = fields.Char()
    date = fields.Datetime(string='Date', required=True, default=lambda self: fields.Datetime.now())
    invoice_type = fields.Selection(string='Type', required=True,
                                    selection=[('in', 'Purchase'),
                                               ('out', 'Sale')])
    invoice_line_ids = fields.One2many(comodel_name='bookstore.invoice.line', inverse_name='invoice_id',
                                       string='Invoice Lines')
    total = fields.Float(string='Total', store=True, compute="_calc_total_invoice")

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


class InvoiceLine(models.Model):
    _name = 'bookstore.invoice.line'
    _description = 'InvoiceLine'

    quantity = fields.Float(string='Quantity', required=True)
    price = fields.Float(string='Price', required=True)
    book_id = fields.Many2one(comodel_name='bookstore.book', string='Book', required=True)
    invoice_id = fields.Many2one(comodel_name='bookstore.invoice', string='Invoice', required=True, ondelete="cascade")
    total = fields.Float(string='Total', compute="_calc_total")

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

    # @api.model
    # def create(self, values):
    #     record = super(bookstore.InvoiceLine, self).create(values)
    #     if record.quantity_in_stock < record.min_quantity:
    #         raise UserError("Kujdes!")
    #     return record
