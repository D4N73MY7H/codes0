from odoo import models, fields, api


class Tag(models.Model):
    _name = 'bookstore.tag'
    _description = 'Bookstore Tag'

    name = fields.Char(string='Tag Name', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)
    color = fields.Integer(String='Color')

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'Tag name must be unique!'),
    ]

    #funksion copy ne odoo
    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        if default is None:
            default = {}
        if not default.get('name'):
            default['name'] = self.name + ' (copy)'
        return super(Tag, self).copy(default)




    # book_ids = fields.Many2many('bookstore.book', string='Books')
