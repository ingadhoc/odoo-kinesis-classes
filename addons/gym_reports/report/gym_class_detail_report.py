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
from openerp import tools

class gym_class_detail_report(osv.osv):
    """"""
    _name = 'gym.class_detail_report'
    _description = "Class Detail Report"
    _auto = False
    _rec_name = 'date'

# No lo puedo hacer asi por dos razones
# 1. los ids que pasa son solo los visibles, pueden ser los primeros 80 de la lista pero el analisis tendía que ser con todo lo filtrado
# 2. no puedo hacer store de este campo function por estar en un report, entocnces no puedo agrupar por este valor
    # def _get_value_percentage(self, cr, uid, ids, name, args, context=None):
    #     result = {}
    #     class_ids = []
    #     for record in self.browse(cr, uid, ids, context=context):
    #         class_id = record.class_id.id
    #         if class_id not in class_ids:
    #             class_ids.append(class_id)
    #     for obj in self.browse(cr, uid, ids, context=context):
    #         # result[obj.id] = 1/len(class_ids)
    #         result[obj.id] = len(class_ids)
    #     return result      

    _columns = {
        'date': fields.date(string='Date', readonly=True),
        'schedule_id': fields.many2one('gym.schedule', 'Schedule', readonly=True),
        'activity_id': fields.many2one('gym.activity', 'Activity', readonly=True),
        'trainer_id': fields.many2one('res.partner', 'Trainer', readonly=True),
        'trainee_id': fields.many2one('res.partner', 'Trainee', readonly=True),
        'class_id': fields.many2one('gym.gym_class', 'Class', readonly=True),
        'value': fields.integer('Value', readonly=True),
        # 'value_percentage': fields.function(_get_value_percentage, string="Value Percentage", type="float", readonly=True,),
        'week_day': fields.selection(selection=[('0', 'Sunday'), ('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('4', 'Thursday'), ('5', 'Friday'), ('6', 'Saturday')], string="Week Day", readonly=True,),
        'class_code': fields.char( 'Class Code', readonly=True,),
        'date_from':fields.function(lambda *a,**k:{}, method=True, type='date',string="Date from"),
        'date_to':fields.function(lambda *a,**k:{}, method=True, type='date',string="Date to"),         
    }

    _order = 'date, schedule_id, activity_id, trainer_id, trainee_id'

    def init(self, cr):

        tools.drop_view_if_exists(cr, 'gym_class_detail_report')
        cr.execute("""
            CREATE OR REPLACE VIEW gym_class_detail_report AS  (

SELECT 
    date, 
    schedule_id, 
    activity_id, 
    class_code, 
    week_day, 
    trainer_id, 
    trainee_id, 
    gym_gym_class_detail.id,
    gym_gym_class.id as class_id,
    value 
FROM gym_gym_class_detail 
INNER JOIN gym_gym_class
ON gym_gym_class_detail.gym_class_id = gym_gym_class.id
)

""")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
