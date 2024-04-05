from odoo import fields, models, api, tools


class MostSoldBooks(models.Model):
    _name = 'bookstore.most.sold.books'
    _description = 'Most Sold Product'
    _auto = False

    employee_name = fields.Char(string='Employee')
    book_title = fields.Char(string='Book')
    category_name = fields.Char(string='Book')
    total_quantity_sold = fields.Float(string='Total Quantity Sold')

    def init(self):
        tools.drop_view_if_exists(self._cr, 'most_sold_books')
        self._cr.execute(f"""CREATE OR REPLACE VIEW {self._table} AS (
                            SELECT
                                e.id AS id,
                                e.name AS employee_name,
                                b.title AS book_title,
                                c.name AS category_name,
                                SUM(il.quantity) AS total_quantity_sold
                            FROM
                                bookstore_invoice_line il
                            JOIN
                                bookstore_invoice i ON il.invoice_id = i.id
                            FULL JOIN
                                bookstore_employee e ON i.employee_id = e.id
                            JOIN
                                bookstore_book b ON il.book_id = b.id
                            JOIN
                                bookstore_book_bookstore_category_rel bc ON b.id = bc.bookstore_book_id
                            JOIN
                                bookstore_category c ON bc.bookstore_category_id = c.id
                            WHERE
                                i.invoice_type = 'out'
                            GROUP BY
                                e.id, e.name, b.title, c.name
                            ORDER BY
                                e.name, SUM(il.quantity) DESC
                                )
                            """)
