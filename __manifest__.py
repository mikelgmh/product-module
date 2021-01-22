# -*- coding: utf-8 -*-
{
    'name': "product_module",

    'summary': """
Gestión de productos""",

    'description': """
Modulo que gestiona los productos que tenemos almacenados en nuestra aplicación, pudiendo
hacer un inventario de ellos, creando nuevos productos, modificandolos y eliminandolos.
""",

    'author': "Aketza, Iker, Mikel, Imanol",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'views/product_module.xml',
        'views/company.xml',
        'views/product.xml',
        'views/user.xml',
        'views/order.xml',
        'report/pm_product_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
