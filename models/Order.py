# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models

class  Order (models.Model):
    __name= 'product-module.order'
    
    date = fields.Date(string="Date order", required=True)
    total_price = fields.Float(string="Total price of the Order")
    status = fields.Selection(selection=[('1', 'REQUESTED'),('2', 'SENDING'),('3', 'RECEIVED'),('4', 'MANAGED')], string="Status of the order", required=True)
