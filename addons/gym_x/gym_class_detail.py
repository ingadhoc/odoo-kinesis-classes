# -*- coding: utf-8 -*-
##############################################################################
#
#    Gym
#    Copyright (C) 2013 Sistemas ADHOC
#    No email
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


import re
from openerp import netsvc
from openerp.osv import osv, fields

class gym_class_detail(osv.osv):
    """"""
    
    _inherit = 'gym.gym_class_detail'

    _sql_constraints = [
        ('trainee_uniq', 'unique(trainee_id, gym_class_id)', 'Trainee must be unique per Class!'),
    ]

    _constraints = [
    ]




gym_class_detail()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
