from odoo import models, fields, api
from odoo.exceptions import ValidationError
import random


class socio(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _description = 'Socios'

    valvulas = fields.Many2one('riegos.valvula')

class valvula(models.Model):
    _name = 'riegos.valvula'
    _description = 'Valvulas'

    cabal = fields.Float()
    servicios = fields.Many2one('riegos.servicio')


class servicio(models.Model):
    _name = 'riegos.servicio'
    _description = 'Servicios'

    horaInicio = fields.Integer()
    horaFinal = fields.Integer()
    cabal = fields.Float()
    valvulas = fields.One2many('riegos.valvulas')
