# -*- coding: utf-8 -*-

from odoo import models, fields, api

class dd_rates(models.Model):
    _inherit='sale.order'
    x_exchange_rate = fields.Float(string='Exchange rate')
#     _name = 'dd_rates.dd_rates'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100