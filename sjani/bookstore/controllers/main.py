from odoo import http
from odoo.exceptions import UserError
from odoo.http import request, Response


class BookstoreAPI(http.Controller):

    @http.route(['/api/data/sell'], auth='public', type='json', methods=['POST'], crsf=False, cors="*")
    def sell_book(self, book_id, quantity, price, invoice_type='out'):
        try:

            book = request.env['bookstore.book'].browse(int(book_id))

            invoice = request.env['bookstore.invoice'].create({
                'invoice_type': invoice_type,
                'invoice_line_ids': [(0, 0, {
                    'quantity': float(quantity),
                    'price': float(price),
                    'book_id': book.id,
                })]
            })

            invoice.confirm()

            return {'result': 'success', 'message': 'Book sold successfully'}
        except UserError as e:
            return {'result': 'error', 'message': str(e)}
