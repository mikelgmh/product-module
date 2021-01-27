# The model reference to Company on the project_module module.
from odoo import models, fields, api, exceptions

# AUTHOR: IKER DE LA CRUZ
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
    # The amount of bosses in the company.
    company_bosses = fields.Integer(
        string='Amount of bosses'
    )

    # The One2Many relation to the res.users.
    user_id = fields.One2many(
        string='Users',
        comodel_name='res.users',
        inverse_name='company_id',
        ondelete='restrict'
    )

    # The constrains to the company_bosses It validates if the amount of users
    # is more than 10.
    @api.constrains('company_bosses')
    def _check_bosses(self):
        for r in self:
            if r.company_bosses < 10:
                raise exceptions.ValidationError(
                    "Insufficient bosses: %s" % r.company_bosses)
