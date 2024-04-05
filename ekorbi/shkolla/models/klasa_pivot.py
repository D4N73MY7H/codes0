from odoo import fields, models, api, tools


class ShkollaKlasaPivot(models.Model):
    _name = 'shkolla.klasa.pivot'
    _description = 'Description'
    _rec_name = 'viti'
    _auto = False


    viti = fields.Selection(
        string='Viti', required=False,
        selection=[('pare', 'I pare'),
                   ('dyte', 'I dyte'),
                   ('trete', 'I trete'), ], )
    grupi = fields.Selection(
        string='Grupi', required=False,
        selection=[('a', 'A'),
                   ('b', 'B'),
                   ('c', 'C'),
                   ('d', 'D'), ], )
    avg_score = fields.Float(string='Class_avg', required=False)

    def init(self):
        tools.drop_view_if_exists(self._cr, 'class_avg_scores_view')
        self._cr.execute(f"""
        CREATE or REPLACE VIEW {self._table}  AS(
        SELECT
            kl.id AS id,
            kl.viti AS viti,
            kl.grupi AS grupi,
            AVG(nota.nota_int) AS avg_score
        FROM
            shkolla_klasa kl
        JOIN
            shkolla_nxenesi nx ON kl.id = nx.klasa_id
        JOIN
            shkolla_nota nota ON nx.id = nota.nxenes_id
        GROUP BY
            kl.id, kl.viti, kl.grupi
        ORDER BY
            AVG(nota.nota_int) DESC
        )""")