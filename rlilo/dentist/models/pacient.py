from odoo import fields, models, api


class DentistiPacient(models.Model):
    _name = 'dentisti.pacient'
    _description = 'Description'
    _rec_name = 'emri'

    emri = fields.Char(string='Emri', required=True)
    mbiemri = fields.Char(string='Mbiemri', required=True)
    nr_tel = fields.Integer(string='Number Telefoni', )
    gr_gjaku = fields.Selection(string='Grupi i gjakuk', required=True,
                                selection=[('a', 'A'),
                                           ('b', 'B'),
                                           ('o', 'O'), ], )
    gjini = fields.Selection(string='Gjini', required=True,
                             selection=[('mashkull', 'Mashkull'),
                                        ('femer', 'Femer'), ], )
    alergji_id = fields.Many2many(comodel_name='dentisti.alergji', string='Alergji')


class DentistiAlergji(models.Model):
    _name = 'dentisti.alergji'

    name = fields.Char(string="Emri alergjie")
