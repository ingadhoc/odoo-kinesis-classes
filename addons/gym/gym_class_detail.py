# -*- coding: utf-8 -*-
##############################################################################
#
#    Gym
#    Copyright (C) 2014 Sistemas ADHOC
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
    
    _name = 'gym.gym_class_detail'
    _description = 'gym_class_detail'

    _columns = {
        'value': fields.integer(string='value', readonly=True),
        'trainee_id': fields.many2one('res.partner', string='Trainee', context={'default_is_trainee':1}, domain=[('is_trainee','=',True)], required=True), 
        'gym_class_id': fields.many2one('gym.gym_class', string='gym_class_id', ondelete='cascade', required=True), 
    }

    _defaults = {
        'value': 1,
    }


    _constraints = [
    ]




gym_class_detail()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
