# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Analytic Tag Default",
    "summary": "Set default values for analytic tags",
    "version": "10.0.1.0.0",
    "category": "Accounting",
    "website": "https://www.camptocamp.com/",
    "author": "Camptocamp SA, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": [
        "account_analytic_default",
    ],
    "data": [
        "views/account_analytic_default.xml",
    ],
    "installable": True,
    "auto_install": False,
}
