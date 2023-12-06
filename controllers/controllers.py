# -*- coding: utf-8 -*-
# from odoo import http


# class TrainingOdoo16(http.Controller):
#     @http.route('/training_odoo16/training_odoo16', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/training_odoo16/training_odoo16/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('training_odoo16.listing', {
#             'root': '/training_odoo16/training_odoo16',
#             'objects': http.request.env['training_odoo16.training_odoo16'].search([]),
#         })

#     @http.route('/training_odoo16/training_odoo16/objects/<model("training_odoo16.training_odoo16"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('training_odoo16.object', {
#             'object': obj
#         })
