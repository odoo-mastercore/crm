# -*- coding: utf-8 -*-
##############################################################################
# Author: Mastercore Sinapsys Global®
# Copyright: 2019-Present.
# License OPL-1 (Odoo Proprietary License v1.0) 
# See https://www.odoo.com/documentation/master/legal/licenses.html
#
###############################################################################

from odoo import Command


def post_init_hook(env):
    """
    Backfill: stages that already had a single team_id should now include that team in team_ids.
    """
    stages = env["crm.stage"].search([("team_id", "!=", False)])
    for stage in stages:
        stage.write({"team_ids": [Command.set(stage.team_id.ids)]})