from odoo import http
from odoo.http import request, Response
import json
import requests


class ShkollaNotatController(http.Controller):

    @http.route('/api/notat/<int:klasa_id>/<string:viti>', type="json", auth="public", methods=['POST'], website=True)
    def get_notat_per_vit(self, klasa_id, viti):
        try:
            notat = request.env['shkolla.nota'].sudo().search_read([
                ('nxenes_id.klasa_id', '=', klasa_id),
                ('viti_shkollor', '=', viti)
            ])

            formatted_notat = []
            for nota in notat:
                formatted_notat.append({
                    'id': nota.id,
                    'nxenesi': nota.nxenes_id.emri,
                    'lenda': nota.lenda,
                    'mesuesi': nota.mesuesi,
                    'nota': nota.nota
                })

            return formatted_notat, 200

        except Exception as e:
            return json.dumps({'error': str(e)}), 500

    @http.route('/api/nxenesit', type="json", auth="public", methods=['POST'], website=True)
    def regjistro_nxenesit(self):
        try:

            request_data = request.jsonrequest

            nxenesi = request.env['shkolla.nxenesi'].sudo().create(request_data)
            return json.dumps({'id': nxenesi.id}), 200

        except Exception as e:
            return json.dumps({'error': str(e)}), 500

    @http.route('/api/fshij_nxenesin/<int:nxenes_id>', type="json", auth="public", methods=['DELETE'], website=True)
    def fshij_nxenesin(self, nxenes_id):
        try:

            nxenesi = request.env['shkolla.nxenesi'].sudo().browse(nxenes_id)

            if nxenesi.exists():
                nxenesi.unlink()
                Response.status = '200'
                return {'message': 'Nxënësi është fshirë me sukses!'}
            else:
                Response.status = '405'
                return {'message': 'Nxënësi nuk ekziston!'}

        except Exception as error:
            request._cr.rollback()
            Response.status = '400'
            return {'message': 'Ndodhi një problem gjatë krijimit: {error}'.format(error=error if error else '')}

    @http.route('/api/update_nxenesin/<int:nxenes_id>', type="json", auth="public", methods=['PUT'], website=True)
    def update_nxenesin(self, nxenes_id):
        try:
            request_data = request.jsonrequest

            nxenesi = request.env['shkolla.nxenesi'].sudo().browse(nxenes_id)

            # if nxenesi:
            #     nxenesi.write({
            #         'emri': request_data.get('emri', nxenesi.emri),
            #         'mbiemri': request_data.get('mbiemri', nxenesi.mbiemri),
            #         'email': request_data.get('email', nxenesi.email),
            #         'tel': request_data.get('tel', nxenesi.tel),
            #         'klasa_id': request_data.get('klasa_id', nxenesi.klasa_id.id)
            #     })
            if nxenesi.exists():
                nxenesi.write(request_data)

                Response.status = '200'
                return {'message': 'Të dhënat e nxënësit janë përditësuar me sukses!'}
            else:
                Response.status = '404'
                return {'message': 'Nxënësi nuk ekziston!'}
        except Exception as error:
            request._cr.rollback()
            Response.status = '400'
            return {'message': 'Ndodhi një problem gjatë përditësimit: {error}'.format(error=error if error else '')}
