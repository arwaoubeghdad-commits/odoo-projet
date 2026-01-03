from odoo import api, fields, models
from odoo.exceptions import ValidationError


class LibraryBook(models.Model):
    _name = "library.book"
    _description = "Livre"

    name = fields.Char(string="Titre", required=True)
    author = fields.Char(string="Auteur")
    isbn = fields.Char(string="ISBN")
    date_publication = fields.Date(string="Date de publication")

    copies_total = fields.Integer(string="Nombre d'exemplaires", default=1)
    active_loan_count = fields.Integer(string="Emprunts en cours", compute="_compute_active_loan_count")
    copies_available = fields.Integer(string="Disponibles", compute="_compute_copies_available")

    loan_ids = fields.One2many("library.loan", "book_id", string="Emprunts")

    @api.depends("loan_ids.state")
    def _compute_active_loan_count(self):
        for rec in self:
            rec.active_loan_count = len(rec.loan_ids.filtered(lambda l: l.state == "ongoing"))

    @api.depends("copies_total", "active_loan_count")
    def _compute_copies_available(self):
        for rec in self:
            rec.copies_available = max(rec.copies_total - rec.active_loan_count, 0)

    @api.constrains("copies_total")
    def _check_copies_total(self):
        for rec in self:
            if rec.copies_total < 0:
                raise ValidationError("Le nombre d'exemplaires doit être positif.")
