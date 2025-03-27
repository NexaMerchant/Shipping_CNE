# -*- coding: utf-8 -*-
# from odoo import http


# class DeliveryCne(http.Controller):
#     @http.route('/delivery_cne/delivery_cne', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/delivery_cne/delivery_cne/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('delivery_cne.listing', {
#             'root': '/delivery_cne/delivery_cne',
#             'objects': http.request.env['delivery_cne.delivery_cne'].search([]),
#         })

#     @http.route('/delivery_cne/delivery_cne/objects/<model("delivery_cne.delivery_cne"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('delivery_cne.object', {
#             'object': obj
#         })

