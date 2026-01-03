from odoo import api, fields, models
from odoo.exceptions import ValidationError


class LibraryLoan(models.Model):
    _name = "library.loan"
    _description = "Emprunt"

    book_id = fields.Many2one("library.book", string="Livre", required=True, ondelete="restrict")
    member_id = fields.Many2one("library.member", string="Adhérent", required=True, ondelete="restrict")

    date_emprunt = fields.Date(string="Date d'emprunt", default=fields.Date.context_today, required=True)
    date_retour_prevue = fields.Date(string="Date retour prévue", required=True)
    date_retour = fields.Date(string="Date retour")

    state = fields.Selection(
        [
            ("ongoing", "En cours"),
            ("returned", "Retourné"),
        ],
        string="Statut",
        default="ongoing",
        required=True,
    )

    is_late = fields.Boolean(string="En retard", compute="_compute_is_late")

    @api.depends("state", "date_retour_prevue")
    def _compute_is_late(self):
        today = fields.Date.context_today(self)
        for rec in self:
            rec.is_late = bool(rec.state == "ongoing" and rec.date_retour_prevue and rec.date_retour_prevue < today)

    @api.constrains("date_emprunt", "date_retour_prevue")
    def _check_dates(self):
        for rec in self:
            if rec.date_retour_prevue and rec.date_emprunt and rec.date_retour_prevue < rec.date_emprunt:
                raise ValidationError("La date de retour prévue doit être supérieure ou égale à la date d'emprunt.")

    @api.constrains("book_id", "state")
    def _check_book_availability(self):
        for rec in self:
            if rec.state != "ongoing" or not rec.book_id:
                continue
            ongoing_count = self.search_count([
                ("book_id", "=", rec.book_id.id),
                ("state", "=", "ongoing"),
                ("id", "!=", rec.id),
            ])
            if ongoing_count + 1 > rec.book_id.copies_total:
                raise ValidationError("Aucun exemplaire disponible pour ce livre.")

    def action_return(self):
        for rec in self:
            rec.write({
                "state": "returned",
                "date_retour": fields.Date.context_today(self),
            })
