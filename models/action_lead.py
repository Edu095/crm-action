# -*- coding: utf-8 -*-

from odoo import models, fields


class Action(models.Model):
    _inherit = 'crm.lead'

    action_lead_ids = fields.One2many('crm.action.lead', 'lead_id', ondelete='cascade')

