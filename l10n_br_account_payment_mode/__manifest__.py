# -*- coding: utf-8 -*-

{
    'name': 'Odoo Brazil Account Banking Payment Infrastructure',
    'version': '10.0.1.0.0',
    'category': 'Banking addons',
    'license': 'AGPL-3',
    'summary': '',
    'description': """ """,
    'author': 'KMEE, '
              'HAEVAS, '
              'Odoo Community Association (OCA)',
    'website': 'http://www.kmee.com.br',
    'depends': [
        'l10n_br_account',
        'l10n_br_data_base',
        'account_due_list_payment_mode',
        'account_payment_order'
    ],
    'data': [
        'views/payment_mode_view.xml',
    ],
    'demo': [
        'demo/payment_demo.xml'
    ],
    'active': False,
    'installable': True,
}
