from odoo import models, fields, api

class ShippingSelectionWizard(models.TransientModel):
    _name = 'shipping.selection.wizard'
    _description = 'Shipping Selection Wizard'

    carrier_id = fields.Many2one('delivery.carrier', string='Shipping Method', required=True)
    sale_order_ids = fields.Many2many('sale.order', string='Sale Orders')

    def apply_shipping(self):
        active_ids = self.env.context.get('active_ids', [])
        orders = self.env['sale.order'].browse(active_ids)
        for order in orders:
            order.write({
                'carrier_id': self.carrier_id.id,
            })
        return {'type': 'ir.actions.act_window_close'}