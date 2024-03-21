from odoo import fields, models, api


class dentistiSherbimet(models.Model):
    _name = 'dentisti.sherbimet'
    _description = 'Description'
    _rec_name = 'e_sherbimi'

    e_sherbimi = fields.Char(string='Emri i Sherbimit', required=True)
    cmimi = fields.Float(string='Cmimi', required=True)
