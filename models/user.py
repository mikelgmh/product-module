from odoo import models

class  User(models.Model):
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

    company_id = fields.Many2one('product-module.company', string="Instructor")


    