# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import requests

class DeliveryCNEDelivery(models.Model):
    _name = 'delivery_cne.delivery_cne'
    _description = 'CNE Delivery'

    name = fields.Char(string='Reference', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    sale_order_id = fields.Many2one('sale.order', string='Sale Order', ondelete='cascade')
    shipping_number = fields.Char(string='Shipping Number', copy=False)
    shipping_status = fields.Char(string='Shipping Status', readonly=True)
    shipping_description = fields.Text(string='Shipping Description', readonly=True)
    carrier_id = fields.Many2one('delivery.carrier', string='Carrier', required=True)

    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('delivery_cne.delivery_cne') or _('New')
        return super(DeliveryCNEDelivery, self).create(vals)

    def action_get_cne_delivery_number(self):
        """Fetch delivery number from CNE API."""
        if not self.carrier_id.cne_brand or not self.carrier_id.cne_packagetype:
            raise ValidationError("CNE Brand and Collection/Delivery Mode must be set on the carrier.")

        # Example payload; adjust according to CNE API specifications
        payload = {
            'brand': self.carrier_id.cne_brand,
            'packagetype': self.carrier_id.cne_packagetype,
            'order_reference': self.sale_order_id.name,
            'destination_zip': self.sale_order_id.partner_shipping_id.zip,
            'destination_country': self.sale_order_id.partner_shipping_id.country_id.code,
            # Add other required fields
        }

        try:
            response = requests.post(
                url="https://api.cne.com/get_delivery_number",
                json=payload,
                timeout=10
            )
            response.raise_for_status()
            data = response.json()
            self.shipping_number = data.get('delivery_number', '')
            self.shipping_status = data.get('status', '')
            self.shipping_description = data.get('description', '')
        except requests.RequestException as e:
            raise ValidationError(f"Error fetching delivery number from CNE API: {e}")