from odoo import api, fields, models

class medicalReservation(models.Model):
    _name = 'medical.reservation'
    _description = 'Manejo de las reservaciones medicas'

    name = fields.Char(string='Nombre del cliente', required=True)
    last_name = fields.Char(string='Apellido', required=True)
    identification_card = fields.Char(string='Cedula', required=True)
    doctor_id = fields.Many2one('doctor.reservation', string='Doctor a reservar')
    date_from = fields.Float(string="Horario de entrada")
    date_to = fields.Float(string="Horario de salida")
    health_insurance = fields.Char(string="Seguro Medico")
    comment = fields.Char(string="Comentario")