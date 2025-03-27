# -*- coding: utf-8 -*-
{
    'name': "Delivery CNE",

    'summary': "Delivery CNE",

    'description': """
Delivery CNE
    """,

    'author': "Steve Liu",
    'website': "https://github.com/xxl4",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Delivery',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'delivery', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/delivery_cne_views.xml',
        'views/sale_order_form_view.xml',
        'data/delivery_data.xml',
        'wizard/choose_delivery_carrier_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

