# Copyright 2018, Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    user_id = fields.Many2one(
        comodel_name='res.users',
        string="Salesperson",
        readonly=True,
    )
