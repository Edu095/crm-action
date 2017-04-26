# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import date


class ActionLead(models.Model):
    _name = 'crm.action.lead'
    _description = _("Action Lead")

    name = fields.Char(string=_("Name"), required=True)
    lead_id = fields.Many2one('crm.lead', string=_("Lead"), index=True, domain="[('type', '=', 'lead')]")
    partner_id = fields.Many2one('res.partner', string=_("Partner"))
    date = fields.Date(default=date.today(), string=_("Date"))
    user_id = fields.Many2one('res.users', ondelete='set null',
                              string=_("Creator"), default=lambda self: self.env.uid)
    action_type = fields.Many2one('crm.action.types', string=_("Action Type"))
    details = fields.Text()
    state = fields.Selection([
        ('draft', _("Pendent")),
        ('done', _("Done")),
    ])

    @api.multi
    def action_draft(self):
        self.state = 'draft'

    @api.multi
    def action_done(self):
        self.state = 'done'
