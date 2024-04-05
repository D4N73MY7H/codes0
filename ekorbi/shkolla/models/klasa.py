from odoo import fields, models, api, tools, _
from odoo.exceptions import ValidationError


class ShkollaKlasa(models.Model):
    _name = 'shkolla.klasa'
    _description = 'Klasa'
    _rec_name = 'viti'
    _auto = False

    viti = fields.Selection(
        string='Viti', required=False,
        selection=[('pare', 'I pare'),
                   ('dyte', 'I dyte'),
                   ('trete', 'I trete'), ], )
    grupi = fields.Selection(
        string='Grupi', required=False,
        selection=[('a', 'A'),
                   ('b', 'B'),
                   ('c', 'C'),
                   ('d', 'D'), ], )
    mesuesi_kujdestar_id = fields.Many2one(comodel_name='shkolla.mesuesi', string='Mesuesi kujdestar', required=False)
    viti_shkollor_id = fields.Many2one(comodel_name='shkolla.viti', string='Viti shkollor', required=False)

    def name_get(self):
        return [(rec.id, "Viti %s, Grupi %s " % (rec.viti, rec.grupi)) for rec in self]


class ShkollaNxenesi(models.Model):
    _name = 'shkolla.nxenesi'
    _inherit = 'mail.thread', 'mail.activity.mixin'
    _description = 'Nxenesi'
    _rec_name = 'emri'

    emri = fields.Char(string='Emri', required=False, tracking=True)
    mbiemri = fields.Char(string='Mbiemri', required=False, tracking=True)
    email = fields.Char(string='Email', required=False, tracking=True)
    tel = fields.Char(string='Tel', required=False, tracking=True)
    klasa_id = fields.Many2one(comodel_name='shkolla.klasa', string='Klasa aktuale', required=False)
    klasa_ids = fields.Many2many(comodel_name='shkolla.klasa', string='Klasat me pare', required=False)
    filename = fields.Char(string='Filename')
    foto = fields.Binary(string="Foto", attachment=True)
    parent_email = fields.Char(string='Emaili Prinderit', required=False)

    # nota_ids = fields.One2many(comodel_name='shkolla.nota',inverse_name='nxenes_id',string='Nota',required=False)

    def name_get(self):
        return [(rec.id, "%s %s " % (rec.emri, rec.mbiemri)) for rec in self]

    def action_share_whatsapp(self):
        if not self.tel:
            raise ValidationError(_("Nr tel gabim"))
        message = 'Hi %s' % self.emri
        whatsapp_api_url = "https://api.whatsapp.com/send?phone=%s&text=%s" % (self.tel, message)
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': whatsapp_api_url
        }


class ShkollaMesuesi(models.Model):
    _name = 'shkolla.mesuesi'
    _description = 'Mesuesi'
    _rec_name = 'emri'

    emri = fields.Char(string='Emri', required=False)
    mbiemri = fields.Char(string='Mbiemri', required=False)
    email = fields.Char(string='Email', required=False)
    tel = fields.Char(string='Tel', required=False)

    def name_get(self):
        return [(rec.id, "%s %s " % (rec.emri, rec.mbiemri)) for rec in self]


class ShkollaVitiShkollor(models.Model):
    _name = 'shkolla.viti'
    _description = 'Viti Shkollor'
    _rec_name = 'viti_shkollor'

    viti_shkollor = fields.Char(string='Viti fillimit', required=False)

    def name_get(self):
        return [(rec.id, "%s " % (rec.viti_shkollor)) for rec in self]

    _sql_constraints = [
        ('unique_viti_shkollor', 'UNIQUE(viti_shkollor)', 'Viti shkollor duhet të jetë unik.'),
    ]


class ShkollaLenda(models.Model):
    _name = 'shkolla.lenda'
    _description = 'Lenda'
    _rec_name = 'emri'

    emri = fields.Char(string='Emri', required=False)
    pershkrim = fields.Text(string="Pershkrim", required=False)

    def name_get(self):
        return [(rec.id, "Lenda %s " % (rec.emri)) for rec in self]


class ShkollaNotat(models.Model):
    _name = 'shkolla.nota'
    _description = 'Notat'
    _rec_name = 'nota'

    nxenes_id = fields.Many2one(comodel_name='shkolla.nxenesi', string='Nxenesi', required=False)
    nota = fields.Selection(
        string='Nota', required=False,
        selection=[('4', 4),
                   ('5', 5),
                   ('6', 6),
                   ('7', 7),
                   ('8', 8),
                   ('9', 9),
                   ('10', 10), ], )
    nota_int = fields.Integer(compute="convert_nota_int", string='Nota int', store=True)
    viti_shkollor = fields.Char(related='klasa_lende_id.klasa_id.viti_shkollor_id.viti_shkollor',
                                string='Viti_shkollor', required=False, store=True)
    klasa_lende_id = fields.Many2one(comodel_name='shkolla.klase_lende', string='Klasa lende mesues', required=False)
    mesuesi = fields.Char(related='klasa_lende_id.mesuesi_id.emri', string='Mesuesi', required=False)
    lenda = fields.Char(related='klasa_lende_id.lenda_id.emri', string='Lenda', required=False)
    lang = fields.Char(string='Lang', required=False)

    @api.constrains('nxenes_id', 'klasa_lende_id')
    def check_nxenesi_klasa_match(self):
        for rec in self:
            if rec.nxenes_id and rec.klasa_lende_id:
                nxenes_klasa = rec.nxenes_id.klasa_id
                klasa_lende = rec.klasa_lende_id
                if nxenes_klasa != klasa_lende.klasa_id:
                    raise ValidationError('Nxënësi dhe klasa në tabelën e notave nuk përputhen!')

    @api.depends('nota')
    def convert_nota_int(self):
        for rec in self:
            rec.nota_int = int(rec.nota)

    def check_grades(self):
        template = self.env.ref('shkolla.parent_mail_template')
        notat = self.env['shkolla.nota'].search([])
        print('hello')
        for n in notat:
            if n.nota_int == 4:
                template.send_mail(n.id)


class ShkollaKlaseLende(models.Model):
    _name = 'shkolla.klase_lende'
    _description = 'Notat'
    _rec_name = 'klasa_id'

    klasa_id = fields.Many2one(comodel_name='shkolla.klasa', string='Klasa ', required=False)
    lenda_id = fields.Many2one(comodel_name='shkolla.lenda', string='Lenda', required=False)
    mesuesi_id = fields.Many2one(comodel_name='shkolla.mesuesi', string='Mesuesi ', required=False)

    def name_get(self):
        return [(rec.id, "Viti %s , Grupi %s, Lenda %s" % (rec.klasa_id.viti, rec.klasa_id.grupi, rec.lenda_id.emri))
                for rec in self]
