# Copyright 2018, Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import api, fields, models


class ProcurementRule(models.Model):
    _inherit = 'procurement.rule'

    @api.multi
    def _prepare_purchase_order(self, product_id, product_qty, product_uom,
                                origin, values, partner):
        res = super()._prepare_purchase_order(
            product_id, product_qty, product_uom, origin, values, partner)
        res['user_id'] = values.get('group_id').sale_id.user_id.id
        return res
