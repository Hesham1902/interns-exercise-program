# File: models/partner.py
from odoo import models, fields

class Partner(models.Model):
    _inherit = 'res.partner'

    is_instructor = fields.Boolean(
        string='Is Instructor',
        default=False,
        help="Check this box if the partner is a course instructor."
    )
    
    # One2many field to show all courses taught by this instructor (REQUIRED for Smart Button)
    course_ids = fields.One2many(
        'academy.course',
        'instructor_id', # <--- This inverse link must match the field in academy_course.py
        string='Taught Courses'
    )