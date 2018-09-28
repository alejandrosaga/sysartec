# -*- coding: utf-8 -*-
{
    'name': "dd_rates",

    'summary': """
        This module calculate exchange rates using 1/x for Odoo values""",

    'description': """
        This module calculate exchange rates using 1/x for Odoo values"
    """,

    'author': "Directiva Digital",
    'website': "http://www.directivadigital.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','bi_manual_currency_exchange_rate'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}