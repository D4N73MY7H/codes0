from odoo import fields, models, api


class TalentsEk(models.Model):
    _name = 'talents.talents_ek'
    _description = 'The model for the student representation'

    name = fields.Char(string='Studenti', required=True)
    nr_amzes = fields.Integer(string='Numri Amzes', required=False)
    nr_rendor = fields.Integer(string='Numri Rendor', required=False)

    # Do te qartesohet nese shkolla do konfigurohet ne DB dhe do te perzjgidhet me vone apo do te jete fushe text
    school_name = fields.Char(string='Emri i shkolles', required=False)
    professor_name = fields.Char(string='Emri i Profesorit', required=False)
    professor_email = fields.Char(string='Email i Profesorit', required=False)
    age = fields.Integer(string='Mosha', required=False)
    student_email = fields.Char(string='Email i Studentit', required=False)
    cel = fields.Char(string='Nr Tel', required=False)
    img_name = fields.Char(string='Image Name')
    image = fields.Binary(string='Imazh', attachment=True)

class ArticleEk(models.Model):
    _name = 'article.article_ek'
    _description = 'The model for the article representation'
    _rec_name = 'title'

    title = fields.Char(string='Titulli i artikullit', required=True)
    author = fields.Char(string='Autori', required=False)
    type = fields.Selection(
        string='Tipi',required=False,
        selection=[('shkencor', 'Shkencor'),
                   ('letrar', 'Letrar'),
                   ('historik', 'Historik'),
                   ('social ekonomik', 'Social ekonomik')])
    publishment_date = fields.Date(string='Data e publikimit', required=False)
    filename = fields.Char(string='Filename')
    article_pdf = fields.Binary(string='Artikulli', attachment=True)
    img_name = fields.Char(string='Image Name')
    image = fields.Binary(string='Imazh', attachment=True)

class TranslationEk(models.Model):
    _name = 'translation.translation_ek'
    _description = 'The model for the translation representation'
    _rec_name = 'title'

    title = fields.Char(string='Titulli',  required=False)
    author = fields.Char(string='Autori', required=False)
    filename = fields.Char(string='Filename')
    translation_pdf = fields.Binary(string='Perkthimi', attachment=True)
    img_name = fields.Char(string='Image Name')
    image = fields.Binary(string='Imazh', attachment=True)
    publishment_date = fields.Date(string='Data e publikimit', required=False)

class PublishmentEk(models.Model):
    _name = 'publishment.publishment_ek'
    _description = 'The model for the publishment representation'
    _rec_name = 'title'

    title = fields.Char(string='Titulli', required=False)
    author = fields.Char(string='Autori', required=False)
    filename = fields.Char(string='Filename')
    publishment_pdf = fields.Binary(string='Botimi', attachment=True)
    publishment_date = fields.Date(string='Data e publikimit', required=False)
    img_name = fields.Char(string='Image Name')
    image = fields.Binary(string='Imazh',  attachment=True)

class ConsultationEk(models.Model):
    _name = 'consultation.consultation_ek'
    _description = 'The model for the consultation representation'

    type  = fields.Selection(string='Tipi', required=False,
                           selection=[('juridike', 'Juridike'),
                                     ('teknike', 'Teknike'),
                                     ('shkencore', 'Shkencore')])
    documents = fields.Many2many('ir.attachment', string='Doukmentet')
    legislation = fields.Many2one(comodel_name='legislation.legislation_ek', string='Legjislacion', required=False)


class LegislationEk(models.Model):
    _name = 'legislation.legislation_ek'
    _description = 'The model for the legislation representation'

    name = fields.Char(string='Emri',required=False)
    description = fields.Text(string="Pershkrimi",required=False)
    legislation_lines_ids = fields.One2many(comodel_name='legislation.lines_ek', inverse_name='legjislacion',string='Legislation lines',required=False)

class LegislationLinesEk(models.Model):
    _name = 'legislation.lines_ek'
    _description = 'The model for the legislation lines representation'

    # paragraph = fields.Char(string='Permbajtja')
    attachment = fields.Many2one('ir.attachment')
    legjislacion = fields.Many2one(comodel_name='legislation.legislation_ek',string='Legjislacion', required=False)

class ProjectEk(models.Model):
    _name = 'project.project_ek'
    _description = 'Project'

    name = fields.Char(string='Emertimi')


class ActivityEk(models.Model):
    _name = 'activity.activity_ek'
    _description = 'Activity'

    name = fields.Char(string='Emertimi')
    paragraph = fields.Text(string="Paragraph", required=False)