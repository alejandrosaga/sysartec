# Copyright 2018, Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Report: Purchase Order',
    'summary': 'Custom report for purchase order',
    'version': '11.0.1.0.0',
    'category': 'Purchase',
    'author': 'Jarsa Sistemas',
    'website': 'https://www.jarsa.com.mx',
    'license': 'AGPL-3',
    'depends': [
        'purchase',
    ],
    'data': [
        'views/report_purchase_order.xml',
        'views/report_paperformat.xml',
        'views/purchase_order_view.xml',
    ],
}
