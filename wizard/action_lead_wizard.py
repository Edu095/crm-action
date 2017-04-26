# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Wizard(models.TransientModel):
    _name = 'crm.action.wizard'

    def _default_lead(self):
        return self.env['crm.lead'].browse(self._context.get('active_ids'))

    lead_id = fields.Many2one('crm.lead', string=_("Lead"), required=True,
                              domain="[('type', '=', 'lead')]", default=_default_lead)
    action_ids = fields.Many2many('crm.action.lead', string=_("Actions"))

    @api.multi
    def add_act(self):
        self.lead_id.action_lead_ids |= self.action_ids
        return {}
