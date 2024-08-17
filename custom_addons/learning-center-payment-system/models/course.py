from odoo import models, fields


class Course(models.Model):
    _name = 'course.course'
    _description = 'Course'

    name = fields.Char(string='Course Name', required=True)
    description = fields.Text(string='Description')
    teacher_ids = fields.Many2many('course.teacher', string='Teachers')
    group_ids = fields.One2many('course.group', 'course_id', string='Groups')
