# -*- coding: utf-8 -*-
# from odoo import http


# class Riegos(http.Controller):
#     @http.route('/riegos/riegos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/riegos/riegos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('riegos.listing', {
#             'root': '/riegos/riegos',
#             'objects': http.request.env['riegos.riegos'].search([]),
#         })

#     @http.route('/riegos/riegos/objects/<model("riegos.riegos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('riegos.object', {
#             'object': obj
#         })
