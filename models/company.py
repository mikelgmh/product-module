# The model reference to Company on the project-module module.
from odoo import models, fields, api


class Company(models.Model):
    # Reference to the odoo's company model to extends.
    _inherit = 'res.company'

    # The company type. It can be ADMIN, PROVIDER or CLIENT.
    company_type = fields.Selection(
        string='Company type',
        selection=[('1', 'ADMIN'), ('2', 'PROVIDER'), ('3', 'CLIENT')],
        required=True
    )
    # The amount of users that contain the company.
    n_users = fields.Integer(
        string='Amount of users',
        default=0
    )

    # The One2Many relation to the project-module.user.
    user_id = fields.One2many(
        string='Users',
        comodel_name='project-module.user',
        inverse_name='' # TODO: relational column of the opposite model
    )
