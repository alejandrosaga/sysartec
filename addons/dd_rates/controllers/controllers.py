# -*- coding: utf-8 -*-
from odoo import http

# class DdRates(http.Controller):
#     @http.route('/dd_rates/dd_rates/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dd_rates/dd_rates/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dd_rates.listing', {
#             'root': '/dd_rates/dd_rates',
#             'objects': http.request.env['dd_rates.dd_rates'].search([]),
#         })

#     @http.route('/dd_rates/dd_rates/objects/<model("dd_rates.dd_rates"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dd_rates.object', {
#             'object': obj
#         })