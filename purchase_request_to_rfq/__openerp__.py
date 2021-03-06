# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Eficent (<http://www.eficent.com/>)
#              <contact@eficent.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
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

{
    "name": "Purchase Request to RFQ",
    "author": "Eficent,"
              "Odoo Community Association (OCA)",
    "version": "1.0",
    "contributors": [
        'Jordi Ballester Alomar',
    ],
    "website": "www.eficent.com",
    "category": "Purchase Management",
    "depends": [
        "purchase_request",
        "purchase"],
    "data": [
        "wizard/purchase_request_line_make_purchase_order_view.xml",
        "views/purchase_request_view.xml",
        "views/purchase_order_view.xml",
    ],
    'demo': [],
    'test': [
        'test/purchase_request_users.yml',
        'test/purchase_request_data.yml',
        'test/purchase_request.yml',
    ],
    "license": 'AGPL-3',
    "installable": True
}
