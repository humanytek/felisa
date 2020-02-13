# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import fields, models


class AccountJournal(models.Model):
    _inherit = "account.journal"

    l10n_mx_edi_amount_authorized_diff = fields.Float(
        'Amount Authorized Difference (Invoice)', limit=1,
        help='This field depicts the maximum difference allowed between a '
        'CFDI and an invoice. When validate an invoice will be verified that '
        'the amount total is the same of the total in the invoice, or the '
        'difference is less that this value.')
