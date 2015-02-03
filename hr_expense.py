# -*- coding: utf-8 -*-
from openerp import models, fields

class AnalyticAccount(models.Model):
    # Add attachments to Analytic Accounts
    _inherit = 'hr.expense.expense'
    attachments_ids = fields.Many2many('ir.attachment', string="Attached documents")
