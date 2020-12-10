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
    company_id = fields.Many2one('product-module.company', string="Instructor")
    product_id = fields.One2many( string="Products", comodel_name="project-module.product", inverse_name="user_id",ondelete="set null")


    