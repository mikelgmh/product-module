from odoo import models

#Relational table between order and product
class  Order_product (models.Model):
    _name= 'product-module.orderProduct'
    
    #Variable related to the order table
    order_id = fields.Many2one('product-module.order', required=True)
    
    #Variable related to the product table
    product_id = fields.Many2one('product-module.product', required=True)
    
    #Variable that indicates the total price of the products
    total_price= fields.Float(string="Total price adding the quantity of products")
    
    #Variable that indicates the total amount of the products
    total_quantity=fields.Float(string="Total quantity of products")