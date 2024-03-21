from odoo import fields, models, api

class Talents_sj(models.Model):
    _name = 'talents.talents_sj'
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

class Article_sj(models.Model):
    _name = 'article.article_sj'
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

class Translation(models.Model):
    _name = 'translation.translation_sj'
    _description = 'The model for the translation representation'
    _rec_name = 'title'

    title = fields.Char(string='Titulli',  required=False)
    author = fields.Char(string='Autori', required=False)
    filename = fields.Char(string='Filename')
    article_pdf = fields.Binary(string='Perkthimi', attachment=True)
    img_name = fields.Char(string='Image Name')
    image = fields.Binary(string='Imazh', attachment=True)
    publishment_date =fields.Date(string='Data e publikimit', required=False)

class Publishment(models.Model):
    _name = 'publishment.publishment_sj'
    _description = 'The model for the publishment representation'
    _rec_name = 'title'

    title = fields.Char(string='Titulli', required=False)
    author = fields.Char(string='Autori', required=False)
    filename = fields.Char(string='Filename')
    article_pdf = fields.Binary(string='Botimi', attachment=True)
    publishment_date = fields.Date(string='Data e publikimit', required=False)
    img_name = fields.Char(string='Image Name')
    image = fields.Binary(string='Imazh',  attachment=True)

class Consultation(models.Model):
    _name = 'consultation.consultation_sj'
    _description = 'The model for the consultation representation'

    type  = fields.Selection(string='Tipi', required=False,
                           selection=[('juridike', 'Juridike'),
                                     ('teknike', 'Teknike'),
                                     ('shkencore', 'Shkencore')])
    documents = fields.Many2many('ir.attachment', string='Doukmentet')
    legislation = fields.Many2one(comodel_name='legislation.legislation_sj', string='Legjislacion', required=False)

class Activity(models.Model):
    _name = 'activity.activity_sj'
    _description = 'Activity'

    name = fields.Char(string='Emertimi')
    paragraph = fields.Text(string="Paragraph", required=False)


class Legislation(models.Model):
    _name = 'legislation.legislation_sj'
    _description = 'The model for the legislation representation'

    name = fields.Char(string='Emri',required=False)
    description = fields.Text(string="Pershkrimi",required=False)
    legislation_lines_ids = fields.One2many(comodel_name='legislation.lines_sj', inverse_name='legjislacion',string='Legislation lines',required=False)

class LegislationLines(models.Model):
    _name = 'legislation.lines_sj'
    _description = 'The model for the legislation lines representation'

    # paragraph = fields.Char(string='Permbajtja')
    attachment = fields.Many2one('ir.attachment')
    legjislacion = fields.Many2one(comodel_name='legislation.legislation_sj',string='Legjislacion', required=False)

class LegalAdvice(models.Model):
    _name = 'legal.advice_sj'
    _description = 'Legal Advice'

    name = fields.Char('Emri', required=True)
    surname = fields.Char('Mbiemri', required=True)
    email = fields.Char('Email', required=True)
    phone_number = fields.Char('Numri i telefonit', required=True)
    message = fields.Char('Mesazhi', required=True)


class Application(models.Model):
    _name = 'application.application_sj'
    _description = 'The model for the application representation'

    name = fields.Char(string='Emri',  required=True)
    surname = fields.Char(string='Mbiemri', required=True)
    email = fields.Char(string='Email', required=True)
    job = fields.Char(string='Profesioni', required=False)
    institution = fields.Char(string='Institucioni', required=False)

    phone_number = fields.Char('Numri i telefonit', required=False)
    content = fields.Char(string='Permbajtja', required=False)
    upload_file = fields.Binary(string="Upload", attachment=False)

    nr_amzes = fields.Integer(string='Numri Amzes', required=True)
    nr_rendor = fields.Integer(string='Numri Rendor', required=True)
    school_name = fields.Char(string='Emri i shkolles', required=True)
    professor_name = fields.Char(string='Emri i Profesorit', required=False)
    professor_email = fields.Char(string='Email i Profesorit', required=False)

    article_id = fields.Many2one(comodel_name='article.article_sj',string='Article',required=False)
    publishment_id = fields.Many2one(comodel_name='publishment.publishment_sj',string='Publishment',required=False)
    translation_id = fields.Many2one(comodel_name='translation.translation_sj',string='Translation',required=False)
    consultation_id = fields.Many2one(comodel_name='consultation.consultation_sj',string='Consultation',required=False)
    translation_id = fields.Many2one(comodel_name='translation.translation_sj',string='Translation',required=False)



