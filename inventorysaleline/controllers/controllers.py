# -*- coding: utf-8 -*-
# from odoo import http


# class Inventorysaleline(http.Controller):
#     @http.route('/inventorysaleline/inventorysaleline/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inventorysaleline/inventorysaleline/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inventorysaleline.listing', {
#             'root': '/inventorysaleline/inventorysaleline',
#             'objects': http.request.env['inventorysaleline.inventorysaleline'].search([]),
#         })

#     @http.route('/inventorysaleline/inventorysaleline/objects/<model("inventorysaleline.inventorysaleline"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inventorysaleline.object', {
#             'object': obj
#         })
