from odoo import fields, models, api

class AccountReportSj(models.AbstractModel):
    _name = 'report.shembull_report.report_account_s'

    @api.model
    def _get_report_values(self, docids, data=None):

        domain = [('invoice_date', '>', data['start_date']), ('invoice_date', '<', data['end_date'])]

        not_paid_invoices = self.env['account.move'].search(domain)

        product_quantities = {}

        for invoice in not_paid_invoices:
            for line in invoice.invoice_line_ids:

                product_id = line.product_id.id
                quantity = line.quantity
                if product_id in product_quantities:
                    product_quantities[product_id] += quantity
                else:
                    product_quantities[product_id] = quantity


        sorted_products = sorted(product_quantities.items(), key=lambda x: x[1], reverse=True)


        most_sold_product_id = sorted_products[0][0] if sorted_products else False


        most_sold_product = self.env['product.product'].browse(most_sold_product_id)


        name = 'Raporti'
        return {
            'docs': [{
                'most_sold_product': most_sold_product.name,
            }],
            'r_name': name,
        }
# from odoo import fields, models, api
#
#
# class AccountReportSj(models.AbstractModel):
#     _name = 'report.shembull_report.report_account_s'
#
#
#     @api.model
#     def _get_report_values(self, docids, data=None):
#         domain = [('invoice_date', '>', data['start_date']), ('invoice_date', '<', data['end_date']), ('payment_state', '=','not_paid' )]
#         name = 'Raporti'
#         not_paid_invoices = self.env['account.move'].search(domain)
#         unpaid_invoices = []
#
#         for rec in not_paid_invoices:
#             unpaid_invoices.append({
#                 'invoice_number': rec.invoice_number,
#                 'invoice_date': rec.invoice_date,
#                 'partner': rec.partner_id.name,
#                 # 'total': rec.amount_total_signed,
#             })
#         return {
#             'docs': unpaid_invoices,
#             'r_name': name,
#         }
#

