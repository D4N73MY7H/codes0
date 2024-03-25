from odoo import models, fields

class Employee(models.Model):
    _name = 'bookstore.employee'
    _description = 'Bookstore Employee'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    address = fields.Text(string='Address')



