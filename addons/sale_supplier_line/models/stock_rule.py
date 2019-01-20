# Copyright 2018, Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

# pylint: disable=C0103

from odoo import models


class ProcurementRule(models.Model):
    _inherit = 'procurement.rule'

    def _make_po_select_supplier(self, values, suppliers):
        """Method overridden from odoo to return the propper supplier info
        searching it taking in consideration the origin sale order"""
        res = super()._make_po_select_supplier(
            values, suppliers)
        currency_id = values.get(
            'move_dest_ids')[0].sale_line_id.purchase_currency_id.id
        sale_id = values.get('group_id').sale_id.id
        supplier = suppliers.with_context(
            sale_id=sale_id, currency_id=currency_id).filtered(
            lambda r: r.sale_order_id and r.sale_order_id.id == r._context.get(
                'sale_id') and r.currency_id.id == r._context.get(
                'currency_id')) or res
        values['supplier'] = supplier
        return supplier
