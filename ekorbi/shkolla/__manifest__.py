{
    'name': 'Shkolla',
    'summary': 'Shkolla- Commprog Version',
    'description': 'Description',
    'category': 'Addons Custom',
    'sequence': -100,
    'author': 'Commprog',
    'website': 'Website',
    'depends': ['base','board','mail'],
    "application": True,
    "installable": True,
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/klasa_view.xml',
        'views/nxenesi.xml',
        'views/mesuesi_view.xml',
        'views/viti_shkollor_view.xml',
        'views/lenda_view.xml',
        'views/notat_view.xml',
        'views/klase_lende_view.xml',
        'views/dashboard_view.xml',
        'views/klasa_pivot_view.xml',
        'data/nota_cron.xml',
        'data/mail_template.xml',
        # 'views/lende_mesues_view.xml',
        # 'wizard/notat_report.xml',
        # 'report/notat_report.xml',
    ],
    'demo': [],
    'auto_install': False
}
