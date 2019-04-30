# Copyright 2019, Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    type_expenses = fields.Selection([
        ('admin', 'Expense administration'),
        ('sale', 'Sale cost'),
        ('weekly', 'Expense sale'), ],
        default='admin', string='Sale cost')
