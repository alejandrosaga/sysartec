# Copyright 2018, Jarsa Sistemas, S.A. de C.V.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Report: Purchase Order',
    'summary': 'Custom report for purchase order',
    'version': '12.0.1.0.0',
    'category': 'Purchase',
    'author': 'Jarsa Sistemas',
    'website': 'https://www.jarsa.com.mx',
    'license': 'LGPL-3',
    'depends': [
        'purchase_stock',
        'base_address_extended',
        'l10n_mx_edi',
    ],
    'data': [
        'views/report_purchase_order.xml',
        'views/report_paperformat.xml',
        'views/purchase_order_view.xml',
    ],
}
