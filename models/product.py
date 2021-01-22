# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models, fields, api, exceptions



class Product (models.Model):
    # The name of the module in Odoo.
    _name = 'product_module.product'

    # The weight of the product.
    quantity = fields.Integer(
        string='Quantity',
        default = 1
    )
    # The unit price of the product.
    price = fields.Float(
        string='Unit Price',
        default = 1
    )
    # The name of the product.
    name = fields.Char(
        string='Name of the product',
        required=True,
        size = 50
    )
    #Total product price 
    total_price = fields.Float(
        string="Total Price", 
        compute='_calculate_total'
    )
        
    # The id of the user that have the product.
    user_id = fields.Many2one(
        string='User',
        comodel_name='res.users',
        required=True,
        default = lambda self: self.env.user
    )
    # The order that contains this product.
    order = fields.One2many(
        string='Order',
        comodel_name='product_module.order_product',
        inverse_name='product_id'
    )

    # Calculate total price field with quantity and price fields
    @api.depends('quantity', 'price')
    def _calculate_total(self):
        for r in self:
            r.total_price = r.quantity * r.price
    
    # Onchange event to warn the user that the price value is incorrect
    @api.onchange('price')
    def _verify__number(self):
        if self.price <= 0:
            return {
                'warning': {
                    'title': "Incorrect price value",'message': 
                    "The number of unit price cant be negative",
                    },
                }
    
    # Onchange event to warn the user that the quantity value is incorrect
    @api.onchange('quantity')
    def _verify__quantity(self):
        if self.quantity <= 0:
            return {
                'warning': {
                    'title': "Incorrect quantity value",'message': 
                    "The number of product quantity must be higher than 0",
                    },
                }
    
    # In case of trying to save quantity and price data with incorrect values, 
    # report the user and restrict the action
    @api.constrains('quantity','price')
    def _check_number(self):
        for record in self:   
            if record.price <= 0:
                raise exceptions.ValidationError("The unit price must be higher than 0")
            if record.quantity <= 0:
                raise exceptions.ValidationError("Number of quantity cant be 0 or less")
    
    # Restrict the action of saving data to database if price value is too high 
    @api.constrains('price')
    def _check_len_price(self):
        number = self.price
        if len(str(abs(number))) > 8:           
            raise exceptions.ValidationError("Wrong value. Your number cant have more than 6 digits and 2 decimal places (maximum price 999,999.99)")
        
    # Restrict the action of saving data to database if quantity value is too high
    @api.constrains('quantity')
    def _check_len_quantity(self):
        number = self.quantity
        if len(str(abs(number))) > 6:           
            raise exceptions.ValidationError("Wrong value. The maximum quantity that can be stored is 999,999")
        
    # Restrict the action  of saving data if product creator is different from current odoo user
    @api.constrains('user_id')
    def _check_product_creator_user(self):
        for record in self:   
            if record.user_id != self.env.user:
                raise exceptions.ValidationError("The user who creates the product must be current user")
                               
    
         
                