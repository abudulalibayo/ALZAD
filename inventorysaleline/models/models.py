# -*- coding: utf-8 -*-


from odoo import models, fields, api



class SaleOrder(models.Model):
    _inherit = "sale.order"
    
        'stock.warehouse', string='Warehouse',
        required=False, readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        default=None, check_company=True)
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
