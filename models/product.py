# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models

class  Product (models.Model):
    # The name of the module in Odoo.
    __name= 'product-module.product'
    # The weight of the product.
    weight = fields.Float(
    string="Product weight")
    # The price of the product.
    price = fields.Double(
    string="Price of the product")
    # The name of the product.
    name = fields.String (
    string="Name of the product", 
    required=True)
    # The id of the user that have the product.
    user_id = fields.Many2One(
    'res.users', 
    string="Users", 
    required=True)
    # The order that contains this product.
    order = fields.One2Many(
    'product-module.order_product',
    'product_id',
    string="Order")