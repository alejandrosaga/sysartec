# Copyright 2018, Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import api, fields, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    user_id = fields.Many2one(
        comodel_name='res.users',
        string="Salesperson",
        compute='_compute_sale_user_id',
        store=True,
    )

    @api.multi
    @api.depends('sale_id', 'purchase_id')
    def _compute_sale_user_id(self):
        for rec in self:
            if rec.sale_id:
                rec.user_id = rec.sale_id.user_id.id
            if rec.purchase_id:
                rec.user_id = rec.purchase_id.user_id.id
