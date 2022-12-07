# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'SportsForecasts',
    'version' : '1.0',
    'summary': 'Sports & Forecasts',
    'sequence': 10,
    'author': 'Kevin COURIAT',
    'description': """
Sports Forecasts
================
Just a simple too to predict sports game
    """,
    'category': 'Technical',
    'website': 'https://couriat.info',
    'images' : [],
    'depends' : ['base'],
    'data': [
        'views/sport_type.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
