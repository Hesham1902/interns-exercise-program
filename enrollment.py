# File: models/enrollment.py
from odoo import models, fields, api

class AcademyEnrollment(models.Model):
    _name = 'academy.enrollment'
    _description = 'Course Enrollment Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # Relational Fields
    course_id = fields.Many2one( # <--- This links back to the course model
        'academy.course', 
        string='Course', 
        required=True, 
        ondelete='cascade'
    )
    student_id = fields.Many2one(
        'res.partner', 
        string='Student', 
        required=True,
        domain=[('is_company', '=', False)]
    )

    # State Field
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    ], string='Status', default='draft', required=True, tracking=True)

    # Basic Fields
    enrollment_date = fields.Date(string='Enrollment Date', default=fields.Date.today)
    notes = fields.Text(string='Notes')

    # Constraints and ORM Methods
    _sql_constraints = [
        ('unique_enrollment', 'UNIQUE(course_id, student_id)', 
         'A student can only be enrolled in a course once.'),
    ]

    def action_confirm(self):
        self.state = 'confirmed'

    def action_cancel(self):
        self.state = 'canceled'
        
    @api.model
    def create(self, vals):
        # Automatically set the enrollment date on creation if not provided
        if not vals.get('enrollment_date'):
            vals['enrollment_date'] = fields.Date.today()
        return super(AcademyEnrollment, self).create(vals)