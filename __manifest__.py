# File: __manifest__.py
{
    "name": "Academy lab 2",
    "version": "17.0.1.0.0",
    "summary": "Training Academy Management",
    "author": "Belal",
    "category": "Education",
    "depends": ["base", "mail"],
    "application": True,
    
    # Define the 'data' list ONCE, in the correct loading order
    'data': [
        # 1. SECURITY (Groups MUST be loaded before CSV/Rules)
        'security/academy_security.xml',        
        'security/ir.model.access.csv',         
        'security/academy_record_rules.xml',    

        # 2. VIEWS (Using the corrected file names)
        'views/academy_menu.xml',
        'views/course_category_views.xml',    
        'views/academy_course_views.xml',
        'views/enrollment_views.xml',         # ***CORRECTED FILE NAME***
        'views/partner_views.xml',            
    ],
}