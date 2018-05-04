# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2013 Agile Business Group sagl
#    (<http://www.agilebg.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import fields, models, api


class AccountVoucherLine(models.Model):
    _inherit = 'account.voucher.line'

    @api.model
    def get_suppl_inv_num(self, move_line_id):
        move_line = self.env['account.move.line'].\
            browse(move_line_id)
        return (move_line.invoice and
                move_line.invoice.supplier_invoice_number or
                '')

    @api.depends('move_line_id', 'voucher_id', 'amount')
    def _compute_supplier_invoice_number(self):
        for line in self:
            if line.move_line_id:
                line.supplier_invoice_number =\
                    self.get_suppl_inv_num(line.move_line_id.id)

    supplier_invoice_number = fields.Char(
        compute='_compute_supplier_invoice_number',
        string='Supplier Invoice Number',
        store=True,
    )
