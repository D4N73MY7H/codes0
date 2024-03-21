from odoo import fields, models, api


class DentistiFatur(models.Model):
    _name = 'dentisti.fatur'
    _description = 'Description'

    staf_id = fields.Many2one(comodel_name='dentisti.staf', string='Dentisti', required=True)
    data = fields.Datetime(string='Data', default=lambda self: fields.Datetime.now(), required=False)
    pacient_id = fields.Many2one(comodel_name='dentisti.pacient', string='Pacienti', required=True)
    trajtmi_lines_ids = fields.One2many(comodel_name='dentisti.trajtmi.lines', inverse_name='fatur_id',
                                        string='fatur line')
    total = fields.Float(string='Total', store=True, compute="_calc_total_invoice")

    @api.depends('trajtmi_lines_ids')
    def _calc_total_invoice(self):
        for fatur in self:
            s = 0
        for fatur_line in fatur.trajtmi_lines_ids:
            s = s + fatur_line.cmime
        fatur.total = s


class DentistiTrajtimLines(models.Model):
    _name = 'dentisti.trajtmi.lines'
    _description = 'Description'

    fatur_id = fields.Many2one(comodel_name='dentisti.fatur', string='Invoice', required=True, ondelete="cascade")
    trajtim_id = fields.Many2one(comodel_name='dentisti.trajtim', string='Trajtim', required=False)
    cmime = fields.Float(string='Cmime', required=True)

    @api.onchange('trajtim_id')
    def _onchange_trajtim_id(self):
        self.cmime = self.trajtim_id.sherbimi_id.cmimi
