from odoo import fields, models, api


class InvoicesjReport(models.TransientModel):
    _name = 'invoicesj.report'


    start_date = fields.Date(default=fields.Datetime.now, string='Start date', required=True)
    end_date = fields.Date(default=fields.Datetime.now, string='End date', required=True)

    def print_report(self):
        self.ensure_one()
        data = {
            "start_date": self.start_date,
            "end_date": self.end_date,
        }
        return self.env.ref('bookstore.action_report_invoicesj').report_action(None, data=data)