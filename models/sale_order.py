from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    _columns = {
        'partner_country_id': fields.Many2one(related='partner_id.country_id', string='Country', store=True),
    }

    partner_country_id = fields.Many2one(related='partner_id.country_id', string='Country', store=True)