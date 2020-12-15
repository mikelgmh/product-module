from odoo import models, fields, api

# Relational table between order and product


class Order_product (models.Model):
    _name = 'product_module.order_product'

    # Variable related to the order table
    order_id = fields.Many2one(
        comodel_name='product_module.order',
        required=True
    )
    # Variable related to the product table
    product_id = fields.Many2one(
        comodel_name='product_module.product',
        required=True
    )

    # Variable that indicates the total price of the products
    total_price = fields.Float(
        string='Total price adding the quantity of products'
    )
    # Variable that indicates the total amount of the products
    total_quantity = fields.Float(
        string='Total quantity of products'
    )
