from odoo import models, fields, api
from odoo.exceptions import UserError


class Book(models.Model):
    _name = 'bookstore.book'
    _description = 'Book Information'
    _rec_name = 'title'

    title = fields.Char(string='Book Title', required=True)
    isbn = fields.Char(string='ISBN')
    publication_year = fields.Integer(string='Publication Year')
    purchase_price = fields.Float(string='Purchase Price', required=True, default=0)
    sale_price = fields.Float(string='Sale Price', required=True, default=0)
    quantity_in_stock = fields.Integer(string='Quantity in Stock')
    min_quantity = fields.Integer(string='Min_quantity', required=False)

    publisher_id = fields.Many2one('bookstore.publisher', string='Publisher')
    author_ids = fields.Many2many('bookstore.author', string='Authors')
    category_ids = fields.Many2many('bookstore.category', string='Categories')



    @api.constrains('quantity_in_stock')
    def check_stock_levels(self):
        for book in self:
            if book.quantity_in_stock < 0:
                raise UserError("Kujdes Sasia eshte e pa mjaftueshme!")
                # pass





    # _sql_constraints = [
    #     ('quantity_in_stock', 'check(quantity_in_stock >= 0)', 'Kujdes sql!'),
    # ]
