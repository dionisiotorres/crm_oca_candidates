# Copyright 2020 Graeme Gellatly
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class CrmStage(models.Model):

    _inherit = "crm.stage"

    required_fields = fields.Many2many(
        comodel_name="ir.model.fields",
        relation="crm_stage_required_fields_rel",
        domain=[("model", "=", "crm.lead")],
        help="Required fields to move an opportuntiy to this stage",
    )
