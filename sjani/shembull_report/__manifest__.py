{
    'name': "Silvester  Report",
    'author': "Communication Progress",
    'website': "web",
    'category': '',
    'version': '1.0',
    'images': [],
    'depends': ['account_accountant'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/silvester_report_view.xml',
        'wizard/sales_report_view.xml',
        'report/silvester_report.xml',
        'report/sales_report.xml',
        # 'wizard/sales_report_view.xml',

             ],
    'demo': [],
    'application': True,
    'installable': True,
}