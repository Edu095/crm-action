# -*- coding: utf-8 -*-
from odoo import http

# class Actions(http.Controller):
#     @http.route('/actions/actions/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/actions/actions/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('actions.listing', {
#             'root': '/actions/actions',
#             'objects': http.request.env['actions.actions'].search([]),
#         })

#     @http.route('/actions/actions/objects/<model("actions.actions"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('actions.object', {
#             'object': obj
#         })
