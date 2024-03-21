from odoo import fields, models, api


class DentistiStaf(models.Model):
    _name = 'dentisti.staf'
    _description = 'Description'
    _rec_name = 'emri'

    emri = fields.Char(string='Emri', required=True)
    mbiemri = fields.Char(string='Mbiemri', required=True)
    email = fields.Char(string='Email', required=True)
    rroga = fields.Integer(string='Rroga', required=True)
    d_punesimi = fields.Date(string='Dita e punesimi', required=True)
    pozicioni = fields.Selection(string='Pozicioni',required=True,
        selection=[('dentisti', 'Dentisti'),
                   ('asistent', 'Asistent'),],
        )
