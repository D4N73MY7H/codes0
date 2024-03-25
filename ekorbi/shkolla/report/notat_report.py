from odoo import fields, models, api
from datetime import datetime


class NotatReport(models.AbstractModel):
    _name = 'report.shkolla.report_notat'
    _description = 'Notat  report'

    @api.model
    def _get_report_values(self, docids, data=None):


        domain = [('viti_shkollor', '=', data['vit_shkollor'])]


        name = 'Notat vjetore'

        rreshta_account_obj = self.env['shkolla.nota'].search(domain)
        rreshta_account = []

        for rec in rreshta_account_obj:
            rreshta_account.append({
                'mesuesi': rec.mesuesi,
                'lenda': rec.lenda,
                'viti': rec.viti_shkollor,

            })
        return {
            'docs': rreshta_account,
            'r_name': name,
        }
