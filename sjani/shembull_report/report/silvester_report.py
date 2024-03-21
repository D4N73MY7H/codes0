from odoo import fields, models, api


class AccountReportSj(models.AbstractModel):
    _name = 'report.shembull_report.report_account_sj'
    _description = 'Account report'

    @api.model
    def _get_report_values(self, docids, data=None):
        domain = [('invoice_date', '>', data['start_date']), ('invoice_date', '<', data['end_date']),
                  ('payment_state', '=', 'not_paid')]
        name = 'Raporti'
        not_paid_invoices = self.env['account.move'].search(domain)
        unpaid_invoices = []

        for rec in not_paid_invoices:
            unpaid_invoices.append({
                'invoice_number': rec.invoice_number,
                'invoice_date': rec.invoice_date,
                'partner': rec.partner_id.name,
                'total': rec.amount_total_signed,
            })
        return {
            'docs': unpaid_invoices,
            'r_name': name,
        }
