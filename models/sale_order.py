from odoo import models, fields,api
import base64

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    order_line_display = fields.Html(
        string='Order Lines', 
        compute='_compute_order_line_display',
        store=False
    )

    @api.depends('order_line', 'order_line.product_id', 'order_line.product_uom_qty')
    def _compute_order_line_display(self):
        for order in self:
            html = '<div style="display: flex; align-items: center;">'
            for line in order.order_line:
                img_src = f'/web/image/product.product/{line.product_id.id}/image_1920'
                html += f'''
                    <div style="margin-right: 10px; text-align: center;">
                        <img src="{img_src}" style="width: 50px; height: 50px;"/>
                        <div>{line.product_id.name}</div>
                        <div>Qty: {line.product_uom_qty}</div>
                    </div>
                '''
            html += '</div>'
            order.order_line_display = html