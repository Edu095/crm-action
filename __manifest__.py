# -*- coding: utf-8 -*-
{
    'name': "CRM Actions",

    'summary': """
        Actions, Action Types
    """,

    'description': """
        Create actions to help categorize actions by types.
        Sets the deadline for that action and receive an email 3 days in advance.
        Display in the calendar.
        Add actions from the leads themselves in the action menu.
    """,

    'author': "RGB",
    'website': "https://www.rgbconsulting.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm', 'mail', 'contacts', 'sale'],

    # always loaded
    'data': [
        # 'security/actions_res_groups_data_security.xml',
        # 'security/actions_rule_data_security.xml',
        'security/ir.model.access.csv',
        'views/actions_views.xml',
        'views/actions_types_views.xml',
        'views/actions_email_templates.xml',
        'views/actions_automated_email_views.xml',
        'views/action_lead_views.xml',
        'views/actions_workflow.xml',
        'wizard/action_lead_wizard_views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
