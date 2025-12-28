# -*- coding: utf-8 -*-
##############################################################################
# Author: Mastercore Sinapsys Global®
# Copyright: 2019-Present.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
#
###############################################################################

from odoo import api, fields, models


class CrmLead(models.Model):
    _inherit = "crm.lead"

    customer_currency_id = fields.Many2one(
        comodel_name="res.currency",
        string="Customer Currency",
        default=lambda self: self.env.company.currency_id,
    )
    amount_customer_currency = fields.Monetary(
        string="Customer amount",
        currency_field="customer_currency_id",
    )
    is_same_currency = fields.Boolean(
        string="Same currency",
        compute="_compute_is_same_currency",
    )

    @api.onchange("customer_currency_id", "amount_customer_currency")
    def _onchange_currency(self):
        for lead in self:
            lead.expected_revenue = lead._get_revenue_in_company_currency()

    def _get_revenue_in_company_currency(self):
        """
        Compute expected revenue in the company currency.

        If the customer's currency equals the company currency,
        then expected revenue matches the customer amount.
        """
        self.ensure_one()
        if self.is_same_currency:
            return self.amount_customer_currency or 0.0

        # In CRM, expected_revenue is expressed in company currency.
        return self.customer_currency_id._convert(
            self.amount_customer_currency or 0.0,
            self.company_currency,
            self.env.company,
            fields.Datetime.now(),
        )

    @api.depends("customer_currency_id", "company_currency")
    def _compute_is_same_currency(self):
        for lead in self:
            lead.is_same_currency = lead.customer_currency_id == (lead.company_currency or self.env.company.currency_id)