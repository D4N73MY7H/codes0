from odoo import models, fields, api


class Category(models.Model):
    _name = 'bookstore.category'
    _description = 'Book Category'

    name = fields.Char(string='Category Name', required=True)
    description = fields.Text(string='Description')

    def action_test(self):
        print("Button Clicked!!!!!!!!!!!!!!!!!!!!!!!!!")
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Click Successful',
                'type': 'rainbow_man',
            }
        }
