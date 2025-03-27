# -*- coding: utf-8 -*-

from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    delivery_cne = fields.Boolean(
        string='CNE Delivery',
        help='Check this box if you want to deliver this order using CNE')
    delivery_cne_ids = fields.One2many(
        'delivery_cne.delivery_cne',
        'sale_order_id',
        string='CNE Deliveries'
    )
    cne_delivery_option = fields.Selection([
        ('standard', 'Standard Delivery'),
        ('express', 'Express Delivery'),
    ], string="CNE Delivery Option")