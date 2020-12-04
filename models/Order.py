from odoo import models

class  Order (models.Model):
    _name= 'product-module.order'
    
    date = fields.Date(string="Date order", required=True)
    total_price = fields.Float(string="Total price of the Order")
    status = fields.Selection(selection=[('1', 'REQUESTED'),('2', 'SENDING'),('3', 'RECEIVED'),('4', 'MANAGED')], string="Status of the order", required=True)

    products_ids=fields.One2Many('product-module.orderProduct','order_id',string="Products")
    #Hay que buscar si hay que eliminar en cascada o no