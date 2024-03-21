{
    'name': 'Formimi Intelektual Shkencor sj',
    'icon': 'formimi_intelektual_shkencor/static/description/foris.png',
    'summary': 'Formimi Intelektual Shkencor - Commprog Version',
    'description': 'Description',
    'category': 'Addons Custom',
    'author': 'Commprog',
    'website': 'Website',
    'license': 'AGPL-3',
    'depends': ['base'],
    "application": True,
    "installable": True,
    'data': [
         'views/talents_view.xml',
         'views/articles_sj_view.xml',
        'views/publishments_view.xml',
         'views/translations_view.xml',
         'views/activities_view.xml',
         'views/applications_view.xml',
        'views/consultations_view.xml'

    ],
    'demo': [],
    'auto_install': False
}