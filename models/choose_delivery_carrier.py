# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

class ChooseDeliveryCarrier(models.TransientModel):
    _inherit = 'choose.delivery.carrier'

    shipping_zip = fields.Char(
        related='order_id.partner_shipping_id.zip',
        string='Shipping Zip',
        readonly=True
    )
    shipping_country_code = fields.Char(
        related='order_id.partner_shipping_id.country_id.code',
        string='Shipping Country Code',
        readonly=True
    )

    is_cne = fields.Boolean(compute='_compute_is_cne')
    cne_last_selected = fields.Char(string="Last Relay Selected")
    cne_last_selected_id = fields.Char(compute='_compute_cne_last_selected_id')
    cne_brand = fields.Char(
        related='carrier_id.cne_brand',
        string='CNE Brand',
        readonly=True
    )
    cne_colLivMod = fields.Char(
        related='carrier_id.cne_packagetype',
        string='CNE Collection/Delivery Mode',
        readonly=True
    )
    cne_allowed_countries = fields.Char(compute='_compute_cne_allowed_countries')

    @api.depends('carrier_id')
    def _compute_is_cne(self):
        for record in self:
            record.is_cne = record.carrier_id.product_id.default_code == "CNE"

    @api.depends('carrier_id', 'order_id.partner_shipping_id')
    def _compute_cne_last_selected_id(self):
        for record in self:
            if record.order_id.partner_shipping_id.is_cne:
                record.cne_last_selected_id = f"{record.shipping_country_code}-{record.order_id.partner_shipping_id.ref.lstrip('CNE#')}"
            else:
                record.cne_last_selected_id = ''

    @api.depends('order_id.partner_shipping_id')
    def _compute_cne_allowed_countries(self):
        for record in self:
            allowed = record.order_id.partner_shipping_id.country_id.name
            record.cne_allowed_countries = allowed

    def action_set_delivery(self):
        """Override to handle CNE deliveries."""
        res = super(ChooseDeliveryCarrier, self).action_set_delivery()
        selected_carrier = self.carrier_id
        if selected_carrier and selected_carrier.product_id.default_code == "CNE":
            # Create a CNE Delivery record
            self.env['delivery_cne.delivery_cne'].create({
                'sale_order_id': self.order_id.id,
                'carrier_id': selected_carrier.id,
                # 'name' will be auto-set via sequence
            })
        return res