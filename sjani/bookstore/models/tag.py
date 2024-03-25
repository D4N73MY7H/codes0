from odoo import models, fields

class Tag(models.Model):
    _name = 'bookstore.tag'
    _description = 'Bookstore Tag'

    name = fields.Char(string='Tag Name', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)
    color = fields.Integer(String='Color')

    # book_ids = fields.Many2many('bookstore.book', string='Books')
