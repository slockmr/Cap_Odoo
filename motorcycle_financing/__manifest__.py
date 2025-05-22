{
	'name': 'Motorcycle Financing',
	'summary': 'Streamlines the loan application process for dealerships.',
	'description': '',
	'license': 'OPL-1',
	'category': 'Kawiil/Custom Modules',
	'author': 'misael',
	'website': 'https://github.com/slockmr/Cap_Odoo.git',
	'version': '18.0.0.0.1',
	'depends': [],
	'data': [
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        "security/rules.xml",
        "views/loan_application_views.xml",
        "views/motorcycle_financing_menu.xml",

    ],
	'demo': ['data/loan_demo.xml'],
	'application': True,
}