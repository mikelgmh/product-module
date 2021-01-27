from odoo import models, fields, api, exceptions

# AUTHOR: MIKEL GRANERO MARTIN DE HIJAS


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

    # The user alias
    alias = fields.Char(
        string='Alias of the user',
        required=True,
        size=50
    )

    # The number of chindren this person has.
    children_number = fields.Integer(
        string='Children',
        default=0
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

    @api.onchange('alias')
    def _verify__alias(self):
        if len(str(self.alias)) < 3:
            return {
                'warning': {
                    'title': "Incorrect length of the alias.", 'message':
                    "The min length is 3.",
                },
            }

    @api.constrains('children_number')
    def _check_max_children(self):
        if self.children_number > 30:
            raise exceptions.ValidationError(
                "Peope with more than 30 children cannot join this company.")
