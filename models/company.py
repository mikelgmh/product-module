# The model reference to Company on the project_module module.
from odoo import models, fields, api


class Company(models.Model):
    # Reference to the odoo's company model to extends.
    _name = 'res.company'
    _inherit = 'res.company'

    # The remaining attributes are defined in res.company.
    # The company type. It can be ADMIN, PROVIDER or CLIENT.
    company_type = fields.Selection(
        string='Company type',
        selection=[('1', 'ADMIN'), ('2', 'PROVIDER'), ('3', 'CLIENT')],
        required=True
    )

    # The One2Many relation to the res.users.
    user_id = fields.One2many(
        string='Users',
        comodel_name='res.users',
        inverse_name='company_id',
        ondelete='restrict'
    )
