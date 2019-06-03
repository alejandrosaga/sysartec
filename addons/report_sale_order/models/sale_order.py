# Copyright 2018, Jarsa Sistemas, S.A. de C.V.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import api, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.multi
    def price_list(self):
        price = []
        for rec in self.mapped('order_line'):
            if rec.list_price:
                price.append(rec.list_price)
        return len(price)
