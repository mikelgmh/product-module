from odoo import models

class  Order_product (models.Model):
    _name= 'product-module.orderProduct'
    
    order_id = fields.Many2one('product-module.order', required=True)
    product_id = fields.Many2one('product-module.product', required=True)
    
    total_price= fields.Float(string="Total price of the Order")
    total_quantity=fields.Float(string="Total quantity of products")