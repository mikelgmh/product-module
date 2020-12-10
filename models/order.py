from odoo import models

"""Storages the orders of the companies. Contais the next values: date of creation,
total price of order and the which is the actual status of the order """
class  Order (models.Model):
    _name= 'product-module.order'
    
    #Date the order was created
    date = fields.Date(
        string="Date order", 
        default=fields.Date.today())
        
    #Total price of the order
    total_price = fields.Float(
        string="Total price of the Order")
    
    #An enumeration indicating which are the types of status
    status = fields.Selection(
        selection=[('1', 'REQUESTED'),
        ('2', 'SENDING'),
        ('3', 'RECEIVED'),
        ('4', 'MANAGED')], 
        string="Status of the order", 
        required=True)

    products=fields.One2Many('product-module.order_product','order_id',string="Products", ondelete='CASCADE')
