from odoo import models, fields


class Group(models.Model):
    _name = 'course.group'
    _description = 'Group'

    name = fields.Char(string='Group Name', required=True)
    course_id = fields.Many2one('course.course', string='Course', required=True)
    teacher_id = fields.Many2one('course.teacher', string='Teacher', required=True)
    student_ids = fields.Many2many('student.student', string='Students')
    payment_ids = fields.One2many('payment.payment', 'group_id', string='Payments')
