# -*- coding: utf-8 -*-
##############################################################################
# Author: Mastercore Sinapsys Global®
# Copyright: 2019-Present.
# License OPL-1 (Odoo Proprietary License v1.0) 
# See https://www.odoo.com/documentation/master/legal/licenses.html
#
###############################################################################

from odoo import Command, fields, models


class CrmStage(models.Model):
    _inherit = "crm.stage"

    team_ids = fields.Many2many("crm.team", string="Sales Teams")

    def write(self, vals):
        """
        Ensure ensuring consistency:
        - If a stage has a team_id, it should be included in team_ids.
        """
        # We must avoid mutating the same 'vals' for all records in a multi-write.
        if "team_ids" in vals:
            return super().write(vals)

        # If at least one record needs a team_ids injection, split writes per record.
        needs_split = any(rec.team_id and rec.team_id not in rec.team_ids for rec in self)
        if not needs_split:
            return super().write(vals)

        for rec in self:
            rec_vals = dict(vals)
            if rec.team_id and rec.team_id not in rec.team_ids:
                rec_vals["team_ids"] = [Command.set(rec.team_id.ids)]
            super(CrmStage, rec).write(rec_vals)
        return True