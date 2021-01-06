# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models, fields, api


class Product (models.Model):
    # The name of the module in Odoo.
    _name = 'product_module.product'

    # The weight of the product.
    quantity = fields.Integer(
        string='Quantity'
    )
    # The price of the product.
    price = fields.Float(
        string='Price'
    )
    # The name of the product.
    name = fields.Char(
        string='Name of the product',
        required=True
    )

    # The id of the user that have the product.
    user_id = fields.Many2one(
        string='User',
        comodel_name='res.users',
        required=True
    )
    # The order that contains this product.
    order = fields.One2many(
        string='Order',
        comodel_name='product_module.order_product',
        inverse_name='product_id'
    )
