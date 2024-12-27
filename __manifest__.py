# -*- coding: utf-8 -*-
{
    'name': "shipping_cne",

    'summary': "Shipping CNE",

    'description': """
Shipping CNE
    """,

    'author': "Steve Liu",
    'website': "https://github.com/NexaMerchant/Shipping_CNE",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory/Delivery',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'delivery', 'stock', 'product', 'purchase', 'account', 'stock_delivery'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'wizard/choose_delivery_carrier_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

