from odoo import models, fields


class TeacherPayment(models.Model):
    _name = 'teacher.payment'
    _description = 'Teacher Payment'

    teacher_id = fields.Many2one('course.teacher', string='Teacher', required=True)
    amount = fields.Float(string='Amount', required=True)
    date = fields.Date(string='Payment Date', required=True, default=fields.Date.context_today)
    description = fields.Text(string='Description')
