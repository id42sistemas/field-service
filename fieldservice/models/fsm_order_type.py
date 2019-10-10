# Copyright (C) 2018 - TODAY, Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class FSMOrderType(models.Model):
    _name = 'fsm.order.type'
    _description = 'Field Service Order Type'

    name = fields.Char(string='Name')