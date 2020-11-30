# -*- coding: utf-8 -*-
from odoo import http

# class Product-module(http.Controller):
#     @http.route('/product-module/product-module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product-module/product-module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product-module.listing', {
#             'root': '/product-module/product-module',
#             'objects': http.request.env['product-module.product-module'].search([]),
#         })

#     @http.route('/product-module/product-module/objects/<model("product-module.product-module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product-module.object', {
#             'object': obj
#         })