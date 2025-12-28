# -*- coding: utf-8 -*-
##############################################################################
# Author: Mastercore Sinapsys Global®
# Copyright: 2019-Present.
# License OPL-1 (Odoo Proprietary License v1.0) 
# See https://www.odoo.com/documentation/master/legal/licenses.html
#
###############################################################################

{
    "name": "CRM stage multiple teams",
    "summary": "Allow multiple sales teams on CRM stages and filter stages accordingly.",
    "description": """
This module extends CRM stages by allowing multiple Sales Teams per stage (Many2many).
It also adapts the stage selection logic on leads and group-by stage behavior so users
only see stages relevant to their teams (or global stages).
    """,
    "version": "19.0.1.0.0",
    "category": "Sales/CRM",
    "author": "Mastercore Sinapsys Global®",
    "website": "https://www.mastercore.us",
    "license": "OPL-1",
    "depends": ["crm"],
    "data": [
        "views/crm_stage_views.xml",
        "views/crm_lead_views.xml",
    ],
    "post_init_hook": "post_init_hook",
    "installable": True,
    "application": False,
}