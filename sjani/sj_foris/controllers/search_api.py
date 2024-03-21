from odoo import fields, models, api, http
from odoo.api import model
from odoo.http import request, Response
from ..controllers.main import models


CONTENT_TYPE = 'application/json;charset=utf-8'

def format_api_body(body):
    modified_records = []
    for record in body:
        for key in record:
            if isinstance(record[key], tuple):
                record[key] = {'id': record[key][0], 'name': record[key][1]}
        modified_records.append(record)
    return modified_records


def format_filter_body(body, filter_param):
    param = ''
    for elem in body:
        param = [elem + (filter_param,)]
    return param


def format_query_params(word):
    special_character = ['ç', 'ë', 'Ç', 'Ë']
    formatted_word = ''
    for i, char in enumerate(word):
        if i == 0:
            if char in special_character:
                continue
            else:
                formatted_word = formatted_word + char
        else:
            if char in special_character:
                break
            else:
                formatted_word = formatted_word + char
    return formatted_word


class GeneralSearchAPI(http.Controller):


    #API FOR SEARCH FROM NAME IN PUBLISHMENT AND TRANSLATION
    @http.route(['/api/search/<string:model_map>'], type="json", auth="public", website=True,
                methods=['POST'], csrf=False, cors="*")
    def get_publishment_fields_list(self, model_map):
        try:
            requestData = request.jsonrequest
            temp_model = models[model_map]
            model = temp_model['model']
            values = temp_model['display_fields']
            offset = (requestData.get('pagination')['currentPage'] - 1) * requestData.get('pagination')['itemsPerPage']
            limit = requestData.get('pagination')['itemsPerPage']

            filter_by_model = temp_model['filter_by']
            filter_by_request = requestData.get('filter_by')
            filter_list = []
            for key, val in filter_by_request.items():
                if key in filter_by_model and val:
                    filter_list.append((key, filter_by_model[key], val))

            records = request.env[model].sudo().search_read(domain=filter_list, fields=values, offset=offset, limit=limit)
            api_body = format_api_body(records)
            Response.status = '200'
            return {
                'amount': len(records),
                'records': api_body
            }

        except Exception as error:
            error_message = 'Ndodhi nje problem! {error}'.format(error=error if error else '')
            Response.status = '400'
            return {'error': error_message}
