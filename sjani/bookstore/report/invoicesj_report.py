from odoo import models, api

class InvoicesjReport(models.AbstractModel):
    _name = 'report.bookstore.report_invoicesj'

    @api.model
    def _get_report_values(self, docids, data=None):
        domain = [('date', '>', data['start_date']), ('date', '<', data['end_date']),
                  ('invoice_id.invoice_type', '=', 'out')]
        name = 'Raporti'
        sold_books = self.env['bookstore.invoice.line'].search(domain)
        report_data = []

        for rec in sold_books:
            report_data.append({
                'invoice_number': rec.invoice_id.invoice_number,
                'invoice_date': rec.date,
                'book_title': rec.book_id.title,
                'quantity': rec.quantity,
                'total': rec.total,
            })
        return {
            'docs': report_data,
            'r_name': name,
        }

class InvoicesjReport(models.AbstractModel):
    _name = 'report.bookstore.report_invoicesj'

    @api.model
    def _get_report_values(self, docids, data=None):
        domain = [('date', '>', data['start_date']), ('date', '<', data['end_date']),
                  ('invoice_id.invoice_type', '=', 'out')]
        name = 'Raporti'
        sold_books = self.env['bookstore.invoice.line'].search(domain)
        report_data = []

        for rec in sold_books:
            report_data.append({
                'invoice_number': rec.invoice_id.invoice_number,
                'invoice_date': rec.date,
                'book_title': rec.book_id.title,
                'quantity': rec.quantity,
                'total': rec.total,
            })
        return {
            'docs': report_data,
            'r_name': name,
        }




