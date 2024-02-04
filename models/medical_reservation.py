from odoo import api, fields, models
from odoo.exceptions import ValidationError
import random


class medicalReservation(models.Model):
    _name = 'medical.reservation'
    _description = 'Manejo de las reservaciones medicas'

    name = fields.Char(string='Codigo Reservacion')
    first_name = fields.Char(string='Nombre del cliente', required=True)
    last_name = fields.Char(string='Apellido', required=True)
    identification_card = fields.Char(string='Cedula', required=True)
    doctor_id = fields.Many2one(
        'doctor.reservation', string='Doctor a reservar')
    date_from = fields.Datetime(string="Horario de entrada")
    date_to = fields.Datetime(string="Horario de salida")
    health_insurance = fields.Char(string="Seguro Medico")
    comment = fields.Char(string="Comentario")

    # Function to Generate a random integer with 8 digits, this is going to be use for generate the code of the reservation.
    @api.model
    def _generate_reservation_code(self):
        return str(random.randint(10**7, 10**8 - 1))

    # Overreding the create function to assign the code when the record is saved.
    @api.model
    def create(self, vals):
        vals['name'] = self._generate_reservation_code()
        res = super(medicalReservation, self).create(vals)
        return res

    @api.constrains('date_from', 'date_to', 'doctor_id')
    def _check_unique_reservations(self):
        for record in self:
            duplicate = True if record.env['medical.reservation'].search_count([('id', '!=', record.id), ('date_to', '>=', record.date_from), (
                'date_from', '<=', record.date_to), ('doctor_id', '=', record.doctor_id.id)]) >= 1 else False
            if duplicate:
                raise ValidationError(
                    "Ya existe una cita agendada con ese doctor en ese rango de hora, por favor elegir otro horario")

    @api.constrains('date_from', 'date_to', 'doctor_id')
    def _check_doctor_schedule(self):
        for record in self:
            # the function fields.Datetime.context_timestamp convert a datetime field to the utc of the logged user
            utc_date_from = fields.Datetime.context_timestamp(
                self, record.date_from)
            utc_date_to = fields.Datetime.context_timestamp(
                self, record.date_to)
            float_date_from = (utc_date_from.hour + utc_date_from.minute / 60)
            float_date_to = (utc_date_to.hour + utc_date_to.minute / 60)
            if (float_date_from < record.doctor_id.date_from) or (float_date_to > record.doctor_id.date_to):
                raise ValidationError(
                    "El doctor no cubre el horario seleccionado para la cita, por favor elegir otro horario")
