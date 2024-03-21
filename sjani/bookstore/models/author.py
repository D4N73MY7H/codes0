from odoo import models, fields, api


class Author(models.Model):
    _name = 'bookstore.author'
    _description = 'Author Information'

    name = fields.Char(string='Author Name', required=True)
    birthdate = fields.Date(string='Birthdate')
    nationality = fields.Char(string='Nationality')
