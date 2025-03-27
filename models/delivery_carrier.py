# -*- coding: utf-8 -*-

from odoo import models, fields

class DeliveryCarrier(models.Model):
    _inherit = 'delivery.carrier'

    cne_brand = fields.Char(string='CNE Brand')
    cne_packagetype = fields.Char(string='CNE Collection/Delivery Mode')