from odoo import models, fields


class Teacher(models.Model):
    _name = 'course.teacher'
    _description = 'Teacher'

    name = fields.Char(string='Teacher Name', required=True)
    subject = fields.Char(string='Subject')
    group_ids = fields.One2many('course.group', 'teacher_id', string='Groups')
    payment_ids = fields.One2many('teacher.payment', 'teacher_id', string='Payments')
