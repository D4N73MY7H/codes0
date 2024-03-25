from odoo import fields, models, api


class SalesReportEk(models.TransientModel):
    _name = 'sales.report_ek'
    _description = 'Description'

    start_date = fields.Date(default=fields.Datetime.now, string='Start date', required=True)
    end_date = fields.Date(default=fields.Datetime.now, string='End date', required=True)

    def print_report(self):
        self.ensure_one()
        data = {
            "start_date": self.start_date,
            "end_date": self.end_date,
        }
        return self.env.ref('account_report_not_paid.action_report_sales_ek').report_action(None, data=data)
