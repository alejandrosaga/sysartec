# Copyright 2019, Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Report: Invoice',
    'summary': 'Custom report for invoice',
    'version': '11.0.1.0.0',
    'category': 'report',
    'author': 'Jarsa Sistemas',
    'website': 'https://www.jarsa.com.mx',
    'license': 'AGPL-3',
    'depends': [
        'l10n_mx_edi',
    ],
    'data': [
        'views/report_invoice.xml',
        'views/report_papaerformat.xml',
    ],
}
