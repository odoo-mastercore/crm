# -*- coding: utf-8 -*-
##############################################################################
# Author: Mastercore Sinapsys Global®
# Copyright: 2019-Present.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
#
###############################################################################

{
    "name": "CRM Lead Currency",
    "summary": "Add the lead amount in the customer's currency and keep expected revenue in company currency.",
    "description": """
On leads/opportunities, this module adds fields to manage the amount in the customer's currency.
When customer currency differs from the company currency, expected revenue is computed in company
currency from the customer amount.
    """,
    "version": "19.0.1.0.0",
    "category": "Sales/CRM",
    "author": "Mastercore Sinapsys Global®",
    "website": "https://www.mastercore.us",
    "license": "AGPL-3",
    "depends": ["crm"],
    "data": [
        "views/crm_lead_views.xml",
    ],
    "installable": True,
    "application": False,
}