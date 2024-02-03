# -*- coding: utf-8 -*-
##############################################################################
#
#    MoviTrack
#    Copyright (C) 2020-TODAY MoviTrack.
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "Citas Medicas",
    "version": "1.0",
    "description": "Modulo para gestion y control de citas medicas con doctores y especialidades",
    "author": "Jose Antonio Andino",
    "depends": [
        "base",
    ],
    "data": [
        "views/root_menu.xml",
        "views/doctor_view.xml",
        "views/medical_reservation_view.xml",
        "views/specialty_view.xml",
        "security/ir.model.access.csv",
    ],
    'installable': True,
}