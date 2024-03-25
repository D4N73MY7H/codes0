from odoo import fields, models, api


class NotatReport(models.TransientModel):
    _name = 'notat.report_ek'
    _description = 'Description'

    vit_shkollor_id = fields.Many2one(comodel_name='shkolla.viti', string='Viti Shkollor', required=True)
    # klasa_lend_mes = fields.Many2one(comodel_name='shkolla.nota', string='Klasa lenda mes', required=True)
    def print_report(self):
        self.ensure_one()
        data = {
            "vit_shkollor": self.env['shkolla.viti'].browse(self.vit_shkollor_id).id,
            # "klasa_lend_mes": self.env['shkolla.nota'].browse(self.klasa_lend_mes).id,

        }
        return self.env.ref('shkolla.action_report_notat_ek').report_action(None, data=data)
