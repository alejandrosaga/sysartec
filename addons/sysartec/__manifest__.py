# Copyright 2019, Jarsa Sistemas, S.A. de C.V.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Sysartec Instance Module',
    'summary': 'Module to configure Sysartec Instance',
    'version': '11.0.1.0.0',
    'category': 'Sale',
    'author': 'Jarsa Sistemas',
    'website': 'https://www.jarsa.com.mx',
    'license': 'LGPL-3',
    'depends': [
        'sale_management',
        'account_accountant',
    ],
    'data': [
        'views/sale_order.xml',
    ],
}