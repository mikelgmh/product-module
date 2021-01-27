from odoo import models, fields, api, exceptions

# Storages the orders of the companies. Contais the next values: date of
# creation, total price of order and the which is the actual status
# of the order.

# AUTHOR: AKETZA ETXEBERRIA


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

    # Onchange event to warn the user that the price value is incorrect
    @api.onchange('total_price')
    def _verify__number(self):
        if self.total_price <= 0:
            return {
                'warning': {
                    'title': "Incorrect total price value", 'message':
                    "The total price can't be less than 0",
                },
            }

    @api.constrains('total_price')
    def _check_order_total_price(self):
        if self.total_price > 1000:
            raise exceptions.ValidationError(
                "Total price must be less than 1000")
