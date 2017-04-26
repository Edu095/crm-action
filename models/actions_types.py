# -*- coding: utf-8 -*-

from odoo import models, fields, _


class ActionTypes(models.Model):
    _name = 'crm.action.types'
    _description = _("Action Types")

    name = fields.Char(string=_("Name"))
    priority = fields.Integer()
    active = fields.Boolean(string=_("Active"))
