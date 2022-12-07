from odoo import models, fields

class day(models.Model):
    _name = "day"
    _description = "Manage day for sports"

    indice = fields.Integer(string="Indice", required=True)
    
