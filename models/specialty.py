from odoo import api, fields, models


class specialtyReservation(models.Model):
    _name = 'specialty.reservation'
    _description = 'Manejo de las diferentes especialidades de los doctores'

    name = fields.Char(string='Nombre', required=True)
    specialty_area = fields.Char(string='Area de especialidad', required=True)
