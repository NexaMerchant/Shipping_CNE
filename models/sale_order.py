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
            products_count = len(order.order_line)
            html = f'''
                <div class="order-line-container">
                    <div class="order-line-header" onclick="this.nextElementSibling.style.display = this.nextElementSibling.style.display === 'none' ? 'flex' : 'none';">
                        <span>{products_count} Products ▼</span>
                    </div>
                    <div class="order-line-content" style="display: none;">
            '''
            
            for line in order.order_line:
                img_src = f'/web/image/product.product/{line.product_id.id}/image_1920'
                html += f'''
                    <div class="product-card">
                        <img src="{img_src}" class="product-image"/>
                        <div class="product-info">
                            <div class="product-name">{line.product_id.name}</div>
                            <div class="product-qty">Qty: {line.product_uom_qty}</div>
                        </div>
                    </div>
                '''
            
            html += '''
                    </div>
                    <style>
                        .order-line-container { width: 100%; }
                        .order-line-header { 
                            cursor: pointer; 
                            padding: 5px;
                            background: #f5f5f5;
                        }
                        .order-line-content { 
                            display: none;
                            flex-wrap: wrap;
                            gap: 10px;
                            padding: 10px;
                        }
                        .product-card {
                            display: flex;
                            align-items: center;
                            border: 1px solid #ddd;
                            padding: 5px;
                            border-radius: 4px;
                        }
                        .product-image {
                            width: 50px;
                            height: 50px;
                            object-fit: contain;
                        }
                        .product-info {
                            margin-left: 10px;
                        }
                        .product-name {
                            font-weight: bold;
                        }
                    </style>
                </div>
            '''
            order.order_line_display = html