# -*- coding: utf-8 -*-
##############################################################################
# Author: Mastercore Sinapsys Global®
# Copyright: 2019-Present.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0)
#
###############################################################################

{
    "name": "CRM Project Create",
    "summary": "Allow create projects from lead/opportunity",
    "description": """
Adds a project link on CRM leads/opportunities and provides a wizard to create a project
from the lead, linking both records and posting origin/destiny messages.
    """,
    "version": "19.0.1.0.0",
    "category": "Sales/CRM",
    "author": "Mastercore Sinapsys Global®",
    "website": "https://www.mastercore.us",
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "crm",
        "sale_project",
        "mail_message_destiny_link_template",
    ],
    "data": [
        "security/ir.model.access.csv",
        "wizards/crm_create_project.xml",
        "views/crm_lead.xml",
    ],
}