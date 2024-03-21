from odoo import fields, models, api


class DentistiTrajtim(models.Model):
    _name = 'dentisti.trajtim'
    _description = 'Description'
    _rec_name = 'pacient_id'

    trajtim = fields.Char(string='Trajtim', required=True)
    pacient_id = fields.Many2one(comodel_name='dentisti.pacient', string='Pacienti', required=False)
    staf_id = fields.Many2one(comodel_name='dentisti.staf', string='Dentisti', required=True, )
    data = fields.Datetime(string='Data', required=True, default=lambda self: fields.Datetime.now())
    sherbimi_id = fields.Many2one(comodel_name='dentisti.sherbimet', string='Sherbimi')
    cmimi_sherbimit = fields.Float(related='sherbimi_id.cmimi', string='Cmimi', store=True)
    seanc_id = fields.Many2one(comodel_name='dentisti.seanc', string='Seanc', required=True)


class DentistiSeanc(models.Model):
    _name = 'dentisti.seanc'
    _description = 'description'

    name = fields.Integer(string='Numri seances', required=True)
