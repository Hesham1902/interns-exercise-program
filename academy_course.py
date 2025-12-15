# File: models/academy_course.py
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class AcademyCourse(models.Model):
    _name = 'academy.course'
    _description = 'Academy Course'
    _inherit = ['mail.thread', 'mail.activity.mixin'] # 1. INHERITANCE: For Chatter and state tracking

    # 1. State/Lifecycle fields
    state = fields.Selection([ # 2. STATE FIELD
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('started', 'Started'),
        ('finished', 'Finished'),
    ], string='Status', default='draft', required=True, tracking=True)

    # 2. Basic Fields
    name = fields.Char(string='Title', required=True, tracking=True)
    code = fields.Char(string='Code', required=True, index=True) # 3. CODE FIELD
    description = fields.Text(string='Description')

    # 3. Numeric/Date Fields
    duration_hours = fields.Float(string='Duration (Hours)')
    max_students = fields.Integer(string='Max Students', default=10)
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')

    # 4. Relational Fields
    instructor_id = fields.Many2one('res.partner', string='Instructor', domain=[('is_instructor', '=', True)])
    category_id = fields.Many2one('academy.course.category', string='Category', required=True)
    enrollment_ids = fields.One2many('academy.enrollment', 'course_id', string='Enrollments') # Links to the new enrollment model
    
    # 5. Computed Fields (REQUIRED)
    enrolled_count = fields.Integer(
        string='Enrolled Count',
        compute='_compute_enrollment_stats',
        store=True # Must be stored to be searchable/groupable
    )
    available_seats = fields.Integer(
        string='Available Seats',
        compute='_compute_enrollment_stats',
        store=True
    )
    is_full = fields.Boolean(
        string='Is Full',
        compute='_compute_enrollment_stats',
        store=True
    )

    # Computed Method: Calculates course capacity
    @api.depends('enrollment_ids.state', 'max_students')
    def _compute_enrollment_stats(self):
        for course in self:
            # Only count 'confirmed' enrollments
            confirmed_enrollments = course.enrollment_ids.filtered(lambda e: e.state == 'confirmed')
            course.enrolled_count = len(confirmed_enrollments)
            
            course.available_seats = course.max_students - course.enrolled_count
            course.is_full = course.available_seats <= 0

    # 6. Constraints and ORM Methods

    # Python Constraint: Check dates and max students
    @api.constrains('max_students', 'start_date', 'end_date')
    def _check_constraints(self):
        for course in self:
            if course.max_students <= 0:
                raise ValidationError("Maximum students must be greater than zero.")
            if course.start_date and course.end_date and course.end_date < course.start_date:
                raise ValidationError("End Date cannot be before the Start Date.")
    
    # SQL Constraint: Course Code must be unique (REQUIRED)
    _sql_constraints = [
        ('code_unique', 'UNIQUE(code)', 'The Course Code must be unique!'),
    ]

    # ORM Method: Auto-convert code to uppercase (REQUIRED)
    @api.onchange('code')
    def _onchange_code(self):
        if self.code:
            self.code = self.code.upper()

    # Workflow Methods (REQUIRED for Statusbar buttons)
    def action_publish(self):
        self.state = 'published'

    def action_start(self):
        self.state = 'started'

    def action_finish(self):
        self.state = 'finished'