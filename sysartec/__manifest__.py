# Copyright 2019, Jarsa Sistemas, S.A. de C.V.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Sysartec Instance Module',
    'summary': 'Module to configure Sysartec Instance',
    'version': '12.0.1.0.0',
    'category': 'Sale',
    'author': 'Jarsa Sistemas',
    'website': 'https://www.jarsa.com.mx',
    'license': 'LGPL-3',
    'depends': [
        'contacts',
        'sale_management',
        'account_accountant',
        'report_sale_order',
        'report_purchase_order',
        'report_invoice_sysartec',
        'sale_purchase_vendor',
    ],
    'data': [
        'security/res_partner_security.xml',
        'views/account_invoice.xml',
        'views/contacts_view.xml',
        'views/sale_order.xml',
    ],
}
