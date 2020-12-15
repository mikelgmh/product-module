from odoo import models, fields, api


class User(models.Model):
    _name = 'res.users'
    _inherit = 'res.users'

    lastAccess = fields.Datetime(
        string='Last access',
        default=fields.Datetime.now
    )
    lastPasswordChange = fields.Datetime(
        string='Last password change'
    )
    privilege = fields.Selection(
        string='Privilege',
        selection=[('1', 'SUPERUSER'), ('2', 'PROVIDER'), ('3', 'WORKER')],
        required=True
    )

    # Relations
    company_id = fields.Many2one(
        string='Instructor',
        comodel_name='res.company'
    )
    product_id = fields.One2many(
        string='Products',
        comodel_name='product_module.product',
        inverse_name='user_id',
        ondelete='set null'
    )
    order_id = fields.One2many(
        string='Orders',
        comodel_name='product_module.order',
        inverse_name='user_id'
    )
