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


{   'active': False,
    'author': u'Sistemas ADHOC',
    'category': u'base.module_category_knowledge_management',
    'demo_xml': [],
    'depends': [u'mail', u'contacts'],
    'description': u'Gym',
    'init_xml': [],
    'installable': True,
    'license': 'AGPL-3',
    'name': u'Gym',
    'test': [],
    'update_xml': [   u'security/gym_group.xml',
                      u'view/gym_class_detail_view.xml',
                      u'view/partner_view.xml',
                      u'view/activity_view.xml',
                      u'view/gym_class_view.xml',
                      u'view/schedule_view.xml',
                      u'view/gym_menuitem.xml',
                      u'data/gym_class_detail_properties.xml',
                      u'data/partner_properties.xml',
                      u'data/activity_properties.xml',
                      u'data/gym_class_properties.xml',
                      u'data/schedule_properties.xml',
                      u'data/gym_class_detail_track.xml',
                      u'data/partner_track.xml',
                      u'data/activity_track.xml',
                      u'data/gym_class_track.xml',
                      u'data/schedule_track.xml',
                      'security/ir.model.access.csv'],
    'version': u'1.1',
    'website': ''}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
