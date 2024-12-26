# -*- coding: utf-8 -*-
# from odoo import http


# class ShippingCne(http.Controller):
#     @http.route('/shipping_cne/shipping_cne', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/shipping_cne/shipping_cne/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('shipping_cne.listing', {
#             'root': '/shipping_cne/shipping_cne',
#             'objects': http.request.env['shipping_cne.shipping_cne'].search([]),
#         })

#     @http.route('/shipping_cne/shipping_cne/objects/<model("shipping_cne.shipping_cne"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('shipping_cne.object', {
#             'object': obj
#         })

