# Copyright 2018, Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    vendor_id = fields.Many2one(
        'res.partner',
        domain="[('supplier', '=', True),('company_type', '=', 'company')]")
    purchase_currency_id = fields.Many2one(
        'res.currency', string='Purchase Currency')

    @api.multi
    def check_lines(self, values):
        self.ensure_one()
        product = self.product_id
        vendor_id = self.vendor_id.id
        purchase_price = self.purchase_price
        currency_id = self.purchase_currency_id.id
        if 'product_id' in values:
            product = self.product_id.browse(values['product_id'])
        if 'vendor_id' in values:
            vendor_id = values['vendor_id']
        if 'purchase_price' in values:
            purchase_price = values['purchase_price']
        if 'purchase_currency_id' in values:
            currency_id = values['purchase_currency_id']
        suppinfo = product.seller_ids.with_context(
            vendor_id=vendor_id, sale_order_id=self.order_id.id).filtered(
                lambda l: l.name.id == l._context['vendor_id'] and
                l.sale_order_id.id == l._context['sale_order_id'])
        vals = {
            'name': vendor_id,
            'product_id': product.id,
            'product_tmpl_id': product.product_tmpl_id.id,
            'price': purchase_price,
            'currency_id': currency_id,
            'sale_order_id': self.order_id.id,
            'delay': 1.0,
            'min_qty': 1.0,
        }
        if suppinfo:
            suppinfo.write(vals)
        else:
            suppinfo.create(vals)

    @api.multi
    def write(self, values):
        for rec in self:
            if (not values.get('vendor_id') and
                    not values.get('purchase_currency_id') and
                    not values.get('purchase_price')):
                continue
            rec.check_lines(values)
        return super().write(values)

    @api.model
    def create(self, values):
        record = super().create(values)
        if (not values.get('vendor_id') and
                not values.get('purchase_currency_id') and
                not values.get('purchase_price')):
            return record
        record.check_lines(values)
        return record
