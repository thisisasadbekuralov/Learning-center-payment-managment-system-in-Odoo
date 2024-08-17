from odoo import models, fields


class Student(models.Model):
    _name = 'student.student'
    _description = 'Student'

    name = fields.Char(string='Student Name', required=True)
    group_ids = fields.Many2many('course.group', string='Groups')
    payment_ids = fields.One2many('payment.payment', 'student_id', string='Payments')
