# Copyright 2018, Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Sale Supplier Line',
    'summary': 'Add supplier in sale order line',
    'version': '12.0.1.0.0',
    'category': 'Sale',
    'author': 'Jarsa Sistemas',
    'website': 'https://www.jarsa.com.mx',
    'license': 'AGPL-3',
    'depends': [
        'sale_margin',
        'purchase_supplierinfo_currency',
    ],
    'data': [
        'views/sale_order_line.xml',
    ],
}
