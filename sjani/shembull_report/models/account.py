from odoo import fields, models, api


class AccountReport(models.Model):

    _description = 'Description'
    _inherit = 'account.move'
