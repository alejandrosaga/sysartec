# Copyright 2018, Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Sale Purchase Vendor',
    'summary': 'Allows to have a vendor in purchase order',
    'version': '11.0.1.0.0',
    'category': 'sale',
    'author': 'Jarsa Sistemas',
    'website': 'https://www.jarsa.com.mx',
    'license': 'AGPL-3',
    'depends': [
        'sale_stock',
    ],
    'data': [
        "views/stock_picking_view.xml",
        "views/purchase_order_view.xml",
    ],
}
