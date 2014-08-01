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
from datetime import datetime

class gym_class(osv.osv):
    """"""
    
    _inherit = 'gym.gym_class'
    _rec_name = 'class_code'

    def _get_week_day(self, cr, uid, ids, name, args, context=None):
        result = {}
        for obj in self.browse(cr, uid, ids, context=context):
            if obj.date:
                # week_day = datetime.strptime(obj.date,'%Y-%m-%d').strftime('%A')
                week_day = datetime.strptime(obj.date,'%Y-%m-%d').strftime('%w')
            result[obj.id] = week_day
        return result

    def _get_class_code(self, cr, uid, ids, name, args, context=None):
        result = {}
        for obj in self.browse(cr, uid, ids, context=context):
            week_day = ''
            if obj.week_day:
                # week_day = datetime.strptime(obj.date,'%Y-%m-%d').strftime('%A')
                # week_day = datetime.strptime(obj.date,'%Y-%m-%d').strftime('%w')
                if obj.week_day == '1':
                    week_day = 'Lunes'
                elif obj.week_day == '2':
                    week_day = 'Martes'
                elif obj.week_day == '3':
                    week_day = 'Miercoles'
                elif obj.week_day == '4':
                    week_day = 'Jueves'
                elif obj.week_day == '5':
                    week_day = 'Viernes'
                elif obj.week_day == '6':
                    week_day = 'Sabado'
                elif obj.week_day == '0':
                    week_day = 'Domingo'
                    
                # week_day = datetime.strptime(obj.date,'%Y-%m-%d').strftime('%A')
            result[obj.id] = obj.activity_id.name + ' - ' + week_day + ' '  + obj.schedule_id.name
        return result

    _columns = {
        # 'week_day': fields.function(_get_week_day, string="Week Day", type="char", readonly=True, store=True),
        'week_day': fields.function(_get_week_day, selection=[('0', 'Sunday'), ('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('4', 'Thursday'), ('5', 'Friday'), ('6', 'Saturday')], string="Week Day", type="selection", readonly=True, store=True),
        'class_code': fields.function(_get_class_code, string="Class Code", type="char", readonly=True, store=True),
    }

    def _get_default_date(self, cr, uid, context=None):
        return fields.date.context_today(self, cr, uid, context=context)

    _defaults = {
        'date': _get_default_date,        
    }

    _constraints = [
    ]

    def on_change_date(self, cr, uid, ids, date, context=None):
        if date:
            week_day = datetime.strptime(date,'%Y-%m-%d').strftime('%w')
        return {'value':{'week_day':week_day}}



gym_class()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
