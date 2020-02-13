# coding: utf-8
{
    'name': 'Felisa',
    'summary': '''
    Instance creator for felisa. This is the app.
    ''',
    'author': 'Vauxoo',
    'website': 'https://www.vauxoo.com',
    'license': 'AGPL-3',
    'category': 'Installer',
    'version': '11.0.0.0.1',
    'depends': [
        "account_accountant",
        "account_voucher",
        "account_move_report",
        "base_automation",
        "board",
        "company_country",
        "crm_project",
        "helpdesk",
        "hr",
        "l10n_mx_edi",
        "l10n_mx_edi_customer_bills",
        "l10n_mx_edi_payment",
        "l10n_mx_edi_vendor_bills",
        "l10n_mx_reports",
        "note",
        "payment",
        "procurement_jit",
        "sale_crm",
        "sale_margin",
        "sale_mrp",
        "stock_landed_costs",
        "website_calendar",
        "stock_mts_mto_rule",
    ],
    'test': [
    ],
    'data': [
        "data/res_lang_data.xml",
        "data/res_company_data.xml",
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
