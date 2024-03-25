import base64
import json

import requests

from odoo import http
from odoo.http import request, Response

models = {

    'article': {
        'fields': ['id', 'title', 'type', 'article_pdf', 'publishment_date', 'image'],
        'filter_by': {'type': '='},
        'fields_pagination': ['id', 'title', 'type', 'article_pdf', 'publishment_date', 'image'],
        'model': 'article.article_ek',
    },
    'publishment': {
        'fields': ['id', 'title', 'publishment_pdf', 'publishment_date', 'image'],
        'fields_pagination': ['id', 'title', 'publishment_pdf', 'publishment_date', 'image'],
        'model': 'publishment.publishment_ek',
        'filter_by': {'title': 'ilike'},
        'display_fields': ['id', 'title']
    },
    'translation': {
        'fields': ['id', 'title', 'translation_pdf', 'publishment_date', 'image'],
        'fields_pagination': ['id', 'title', 'translation_pdf', 'publishment_date', 'image'],
        'model': 'translation.translation_ek',
        'filter_by': {'title': 'ilike'},
        'display_fields': ['id', 'title']
    },
    'talents': {
        'fields': ['id', 'name', 'student_email', 'cel', 'image', 'age'],
        'fields_pagination': ['id', 'name', 'student_email', 'cel', 'image', 'age'],
        'model': 'talents.talents_ek',
        'filter_by': {},
    }
}


def format_api_body(body):
    modified_records = []
    for record in body:
        for key in record:
            if isinstance(record[key], tuple):
                record[key] = {'id': record[key][0], 'name': record[key][1]}
        modified_records.append(record)
    return modified_records


CONTENT_TYPE = 'application/json;charset=utf-8'


class ForisAPI(http.Controller):

    # API FOR PAGINATION FOR ALL DATA / IMAGE AND PDF
    @http.route(['/api/data/<string:model>'],
                type="json", auth="public", methods=['POST'], website=True, csrf=False, cors="*")
    def get_paginated_data(self, model):
        try:
            orm_model = models[model]
            requestData = request.jsonrequest
            filter_by_model = orm_model.get('filter_by', [])
            filter_by_request = requestData.get('filter_by', [])
            filter_list = []
            for key, val in filter_by_request.items():
                if key in filter_by_model and val:
                    filter_list = [(key, filter_by_model[key], val)]
            # Formula e paginimit
            if requestData.get('pagination'):
                current_page = requestData.get('pagination')['currentPage']
                items_per_page = requestData.get('pagination')['itemsPerPage']
                if current_page and items_per_page:
                    offset = (current_page - 1) * items_per_page
                    limit = items_per_page
                    ###
                    records = request.env[orm_model['model']].sudo().search_read(
                        filter_list, offset=offset, limit=limit, fields=orm_model['fields_pagination'])

                    if records:
                        for rec in records:
                            rec.update(
                                {key: value.decode() if isinstance(value, (bytes, bytearray)) else value for key, value
                                 in
                                 rec.items()})
                else:
                    records = request.env[orm_model['model']].sudo().search_read(
                        filter_list, fields=orm_model['fields_pagination'])

                api_body = format_api_body(records)
                Response.status = '200'
                return {
                    'amount': request.env[orm_model['model']].sudo().search_count(filter_list),
                    'records': api_body,
                }
            else:
                Response.status = '400'
                return {'message': 'Ndodhi një problem, nuk ka pagination!'}

        except Exception as error:
            error_message = 'Ndodhi nje problem! {error}'.format(error=error if error else '')
            Response.status = "400"
            return {'error': error_message}


    @http.route(['/api/<string:var>'], auth="public", type="json", methods=['POST'], csrf=False, cors="*")
    def create(self, var):
        try:
            request_data = request.jsonrequest
            model_class = models[var]
            model = model_class['model']
            record = request.env[model].sudo().create(request_data)
            Response.status = '200'
            return {'id': record.id}
        except Exception as error:
            request._cr.rollback()
            Response.status = '400'
            return {'message': 'Ndodhi një problem gjatë krijimit: {error}'.format(error=error if error else '')}