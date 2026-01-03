from odoo import fields, models


class LibraryMember(models.Model):
    _name = "library.member"
    _description = "Adhérent"

    name = fields.Char(string="Nom complet", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Téléphone")
    active = fields.Boolean(default=True)

    loan_ids = fields.One2many("library.loan", "member_id", string="Emprunts")
