from odoo import models, fields, api

# Storages the orders of the companies. Contais the next values: date of
# creation, total price of order and the which is the actual status
# of the order.


class Order (models.Model):
    _name = 'product_module.order'

    # Date the order was created
    date = fields.Date(
        string='Date order',
        default=fields.Date.context_today
    )
    # Total price of the order
    total_price = fields.Float(
        string='Total price of the Order'
    )
    # An enumeration indicating which are the types of status
    status = fields.Selection(
        string='Status of the order',
        selection=[('1', 'REQUESTED'), ('2', 'SENDING'),
                   ('3', 'RECEIVED'), ('4', 'MANAGED')],
        required=True
    )

    # Reference to the relation table between orders and products
    products = fields.One2many(
        string='Products',
        comodel_name='product_module.order_product',
        inverse_name='order_id',
        ondelete='cascade'
    )
    # References the user model
    user_id = fields.Many2one(
        string='User',
        comodel_name='res.users'
    )
