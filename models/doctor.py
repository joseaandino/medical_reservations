from odoo import api, fields, models

class doctorReservation(models.Model):
    _name = 'doctor.reservation'
    _description = 'Manejo de los doctores'

    name = fields.Char(string='Nombre', required=True)
    last_name = fields.Char(string='Apellido', required=True)
    identification = fields.Char(string='Identificación', required=True)
    specialty_ids = fields.Many2many('specialty.reservation', string="Especialidades")
    date_from = fields.Float(string="Horario de entrada")
    date_to = fields.Float(string="Horario de salida")


