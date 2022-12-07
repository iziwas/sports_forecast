from odoo import models, fields


class Type(models.Model):
    _name = 'sport.type'
    _description = 'List of sports'

    name = fields.Char(string="Name", required=True)