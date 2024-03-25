from odoo import fields, models, api


class SalesReportEk(models.AbstractModel):
    _name = 'report.account_report_not_paid.ek_report_sales'
    _description = 'Sales  report'

    @api.model
    def _get_report_values(self, docids, data=None):
        domain = [('move_id.invoice_date', '>=', data['start_date']), ('move_id.invoice_date', '<', data['end_date']), ('move_id.move_type','=','out_invoice')]

        name = 'Sales Report'


        rreshta_inv_line=self.env['account.move.line'].search(domain)
        prod_info={}
        rreshta_account = []


        for rec in rreshta_inv_line:
            if rec.product_id.name in prod_info:
                prod_info[rec.product_id.name] +=rec.quantity
            else:
                prod_info[rec.product_id.name] = rec.quantity

        sorted_prod = sorted(prod_info.items(), key=lambda x: x[1], reverse=True)

        for prod_name, total_quantity in sorted_prod:
            rreshta_account.append({
                'produkti': prod_name,
                'sasia': total_quantity,
            })
        return {
            'docs': rreshta_account,
            'r_name': name,
        }
