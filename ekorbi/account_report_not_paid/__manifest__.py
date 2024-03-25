{
    'name': 'Account Report Not Paid',
    'version': '11.0.1.1.1',
    'category': 'Accounting/Accounting',
    'summary': 'Raporte Financiare',
    "author": "Commprog",
    "depends": ['account_accountant'],
    "application": True,
    'auto_install': False,
    "installable": True,
    "data": [
        # 'views/account_view.xml',
        'report/account_report.xml',
        'wizard/account_report.xml',
        'report/sales_report.xml',
        'wizard/sales_report.xml',
    ],

}
