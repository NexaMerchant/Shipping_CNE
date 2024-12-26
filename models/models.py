# -*- coding: utf-8 -*-

from odoo import models, fields, api


class shipping_cne(models.Model):
    _name = 'shipping_cne.shipping_cne'
    _description = 'shipping_cne.shipping_cne'

    name = fields.Char()
    date = fields.Date()
    shipping = fields.Char()
    shipping_type = fields.Char()
    shipping_number = fields.Char()
    shipping_weight = fields.Float()
    shipping_price = fields.Float()
    shipping_currency = fields.Char()
    shipping_status = fields.Char()
    shipping_description = fields.Text()
    shipping_user = fields.Many2one('res.users', string='User')
    shipping_partner = fields.Many2one('res.partner', string='Partner')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('shipping_cne.shipping_cne') or '/'
        return super(shipping_cne, self).create(vals)
    
    @api.model
    def _get_default_user(self):
        return self.env['res.users'].browse(self._uid)
    
    @api.model
    def _get_default_partner(self):
        return self.env['res.partner'].browse(self._uid)
    
