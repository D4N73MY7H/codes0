from odoo import fields, models, api


class AccountReportEk(models.AbstractModel):
    _name = 'report.account_report_not_paid.ek_report_account'
    _description = 'Account  report'

    @api.model
    def _get_report_values(self, docids, data=None):
        domain = [('invoice_date', '>=', data['start_date']), ('invoice_date', '<', data['end_date']), ('payment_state', '=','not_paid')]

        name='Not Paid Report'

        rreshta_account_obj = self.env['account.move'].search(domain)
        rreshta_account = []

        for rec in rreshta_account_obj:
            rreshta_account.append({
                'invoice_number': rec.invoice_number,
                'invoice_date': rec.invoice_date,
                'partner': rec.partner_id.name,
                'total': rec.amount_total_signed,
            })
        return {
            'docs': rreshta_account,
            'r_name': name,
        }