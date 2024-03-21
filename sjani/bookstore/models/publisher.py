from odoo import models, fields, api


class Publisher(models.Model):
    _name = 'bookstore.publisher'
    _description = 'Publisher Information'

    name = fields.Char(string='Publisher Name', required=True)
    address = fields.Text(string='Address')
    contact_details = fields.Char(string='Contact Details')
