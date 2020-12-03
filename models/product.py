# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models

class  Product (models.Model):
    __name= 'product-module.product'
    
    weight = fields.Float(string="Product weight", required=True)
    price = fields.Double(string="Price of the product", required=True)
    name = fields.String (string="Name of the product", required=True)
