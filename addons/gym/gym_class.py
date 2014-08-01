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

class gym_class(osv.osv):
    """"""
    
    _name = 'gym.gym_class'
    _description = 'gym_class'

    _columns = {
        'date': fields.date(string='Date', required=True),
        'trainer_id': fields.many2one('res.partner', string='Trainer', context={'default_is_trainer':1}, domain=[('is_trainer','=',True)], required=True), 
        'schedule_id': fields.many2one('gym.schedule', string='Schedule', required=True), 
        'activity_id': fields.many2one('gym.activity', string='Activity', required=True), 
        'gym_class_detail_ids': fields.one2many('gym.gym_class_detail', 'gym_class_id', string='Class Detail'), 
    }

    _defaults = {
    }


    _constraints = [
    ]




gym_class()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
