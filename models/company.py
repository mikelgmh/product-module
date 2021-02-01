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
    number_of_employees = fields.Integer(
        string='Amount of employees',
        readonly=True,
        compute='_number_of_employees'
    )

    # The One2Many relation to the res.users.
    employees = fields.One2many(
        string='Users',
        comodel_name='res.users',
        inverse_name='company_id',
        ondelete='restrict'
    )

    # The constrains to the number_of_employees It validates if the amount of
    # users is less than 100.
    @ api.constrains('number_of_employees')
    def _check_bosses(self):
        for r in self:
            if r.number_of_employees > 100:
                raise exceptions.ValidationError(
                    "More employees than expected (<100): %s"
                    % r.number_of_employees
                )

    # The multi to the count the number of employees and insert into the
    # number_of_employees field.
    @api.multi
    def _number_of_employees(self):
        for data in self:
            data.number_of_employees = len(data.employees)
