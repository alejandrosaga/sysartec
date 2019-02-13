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
        if values.get('sale_line_id'):
            sale_line = self.env['sale.order.line'].browse(
                values['sale_line_id'])
        else:
            sale_line = values['move_dest_ids'].sale_line_id
        currency_id = sale_line.purchase_currency_id.id
        sale_id = sale_line.order_id.id
        vendor_id = sale_line.vendor_id.id
        supplier = suppliers.with_context(
            sale_id=sale_id, currency_id=currency_id,
            vendor_id=vendor_id).filtered(
            lambda r: r.sale_order_id and r.sale_order_id.id == r._context.get(
                'sale_id') and r.currency_id.id == r._context.get(
                'currency_id' and r.name.id == r._context.get('vendor_id'))
            ) or res
        values['supplier'] = supplier
        return supplier
