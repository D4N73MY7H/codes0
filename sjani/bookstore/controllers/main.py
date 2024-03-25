from odoo import http
from odoo.exceptions import UserError
from odoo.http import request, Response
import json


class BookstoreAPI(http.Controller):

    # delete
    @http.route('/api/delete_book/<int:book_id>', type="json", auth="public", methods=['DELETE'], website=True)
    def delete_book(self, book_id):
        try:

            book = request.env['bookstore.book'].sudo().browse(book_id)

            if book.exists():
                book.unlink()
                return {'message': 'Librii është fshirë me sukses!'}, 200
            else:
                return {'error': 'Libri nuk ekziston!'}, 404


        except Exception as e:
            return {'error': str(e)},

        # create

    @http.route('/api/create_book', type="json", auth="public", methods=['POST'], website=True)
    def create_book(self):
        try:

            request_data = request.jsonrequest

            if 'title' not in request_data or 'purchase_price' not in request_data or 'sale_price' not in request_data:
                return json.dumps({'error': 'Missing required fields!'}), 400

            book = request.env['bookstore.book'].sudo().create({
                'title': request_data['title'],
                'purchase_price': request_data['purchase_price'],
                'sale_price': request_data['sale_price'],
                'quantity_in_stock': request_data['quantity_in_stock'],
                'min_quantity': request_data['min_quantity'],
                'publication_year': request_data['publication_year'],

            })

            return {'message': 'Book created successfully', 'book_id': book.id}, 201

        except Exception as e:
            return {'error': str(e)}, 500

    # @http.route('/api/get_low_stock_books', type="json", auth="public", methods=['GET'], website=True)
    # def get_low_stock_books(self):
    #     try:
    #
    #         books = request.env['bookstore.book'].sudo().search([('quantity_in_stock', '<', 'min_quantity')])
    #         book_data = []
    #
    #         for book in books:
    #             book_data.append({
    #                 'title': book.title,
    #                 'quantity_in_stock': book.quantity_in_stock,
    #                 'min_quantity': book.min_quantity,
    #             })
    #
    #         return json.dumps({'books': book_data}), 200
    #
    #     except Exception as e:
    #         return json.dumps({'error': str(e)}), 500

    # list me low quantity books
    # @http.route('/api/get_low_stock_books', type="json", auth="public", methods=['GET'], website=True)
    # def get_low_stock_books(self):
    #     try:
    #         books = request.env['bookstore.book'].sudo().search([])
    #         low_stock_books = []
    #         for book in books:
    #             if book.quantity_in_stock <= book.min_quantity:
    #                 low_stock_books.append({
    #                     'title': book.title,
    #                     'quantity_in_stock': book.quantity_in_stock,
    #                     'min_quantity': book.min_quantity,
    #                 })
    #
    #         return {'books': low_stock_books}, 200
    #
    #     except Exception as e:
    #         return {'error': str(e)}, 500


    #filterd
    @http.route('/api/get_low_stock_books', type="json", auth="public", methods=['GET'], website=True)
    def get_low_stock_books(self):
        try:

            # books = request.env['bookstore.book'].sudo().search([]).filtered(
            #     lambda book: book.quantity_in_stock <= book.min_quantity, order='quantity_in_stock asc', limit=1
            # )
            # books = request.env['bookstore.book'].sudo().search([('quantity_in_stock', '<=', 3)],
            #                                                     offset=0, limit=1, order=None, count=False).filtered(
            #     lambda book: book.quantity_in_stock <= book.min_quantity)
            books = request.env['bookstore.book'].sudo().search([]).filtered(lambda book: book.quantity_in_stock <= book.min_quantity)
            low_stock_books = []
            for book in books:
                    low_stock_books.append({
                        'title': book.title,
                        'quantity_in_stock': book.quantity_in_stock,
                        'min_quantity': book.min_quantity,
                    })

            return {'books': low_stock_books}, 200

        except Exception as e:
            return {'error': str(e)}, 500

    # shit/blerje
    @http.route('/api/sell_book', type="json", auth="public", methods=['POST'], website=True)
    def sell_book(self):
        try:
            request_data = request.jsonrequest

            if 'book_id' not in request_data or 'quantity' not in request_data or 'price' not in request_data or 'invoice_type' not in request_data:
                return json.dumps({'error': 'Missing required fields!'}), 400

            book_id = request_data['book_id']
            quantity = request_data['quantity']
            price = request_data['price']
            invoice_type = request_data['invoice_type']

            book = request.env['bookstore.book'].sudo().browse(book_id)

            if not book:
                return json.dumps({'error': 'Book not found!'}), 404

            invoice = request.env['bookstore.invoice'].sudo().create({
                'invoice_type': invoice_type,
                'invoice_line_ids': [(0, 0, {
                    'quantity': quantity,
                    'price': price,
                    'book_id': book.id,
                })]
            })

            invoice.confirm()

            return json.dumps({'message': 'Book transaction completed successfully', 'invoice_id': invoice.id}), 201

        except Exception as e:
            return json.dumps({'error': str(e)}), 500

        # update book

    @http.route('/api/update_book/<int:book_id>', type="json", auth="public", methods=['PUT'], website=True)
    def update_book(self, book_id):
        try:
            request_data = request.jsonrequest
            book = request.env['bookstore.book'].sudo().browse(book_id)
            if book.exists():
                book.write(request_data)

                return json.dumps({'message': 'Book has been updated successfully', 'book_id': book.id}), 200
            else:
                Response.status = 400
                return {'error': 'Nuk egziston'}

        except Exception as e:
            return json.dumps({'error': str(e)}), 500

    # @http.route('/api/sell_book', type="json", auth="public", methods=['POST'], website=True)
    # def sell_book(self):
    #     try:
    #         request_data = request.jsonrequest
    #
    #         # if 'book_id' not in request_data or 'quantity' not in request_data or 'price' not in request_data:
    #         #     return json.dumps({'error': 'Missing required fields!'}), 400
    #
    #         book_id = int(request_data['book_id'])
    #         quantity = float(request_data['quantity'])
    #         price = float(request_data['price'])
    #
    #         book = request.env['bookstore.book'].sudo().browse(book_id)
    #
    #         # if not book:
    #         #     return json.dumps({'error': 'Book not found!'}), 404
    #
    #         invoice_type = request_data.get('invoice_type', 'out')
    #
    #         # Use sudo to elevate privileges for creating the invoice
    #         invoice = request.env['bookstore.invoice'].sudo().create({
    #             'invoice_type': invoice_type,
    #             'invoice_line_ids': [(0, 0, {
    #                 'quantity': quantity,
    #                 'price': price,
    #                 'book_id': book.id,
    #             })]
    #         })
    #
    #         invoice.confirm()
    #
    #         return json.dumps({'message': 'Book sold successfully', 'invoice_id': invoice.id}), 201
    #
    #     except Exception as e:
    #         return json.dumps({'error': str(e)}), 500
