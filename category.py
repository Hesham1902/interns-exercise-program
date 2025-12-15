# File: models/category.py
from odoo import models, fields, api

class AcademyCourseCategory(models.Model):
    _name = 'academy.course.category'
    _description = 'Academy Course Category'

    name = fields.Char(string='Category Name', required=True)
    description = fields.Text(string='Description')

   
    course_ids = fields.One2many(
        'academy.course', 
        'category_id', 
        string='Courses in Category'
    )
    
   
    course_count = fields.Integer(
        string='Number of Courses',
        compute='_compute_course_count',
        store=True # Stored to be easily searchable
    )

    # Computed Method
    @api.depends('course_ids') 
    def _compute_course_count(self):
        for category in self:
            category.course_count = len(category.course_ids)