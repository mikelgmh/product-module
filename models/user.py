from odoo import models

class User(models.Model):
    _inherit = "res.users";
    

    lastAccess = fields.Datetime(string="Last access",default=fields.Datetime.now())
    lastPasswordChange = fields.Datetime(string="Last access",default=null)
    #Enum Privilege
    privilege = fields.Selection(
        selection=[
        ('1','SUPERUSER'),
        ('3','WORKER'),
        ('2','PROVIDER')],
        string="privilege",
        required=True)

    #Relations
    company_id = fields.Many2one('res.company', string="Instructor")
    product_id = fields.One2many( string="Products", comodel_name="res.product", inverse_name="user_id",ondelete="set null")
    order_id = fields.One2many( string="Orders", comodel_name="res.order", inverse_name="user_id",ondelete="set null")


    