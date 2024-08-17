from odoo import models, fields


class Payment(models.Model):
    _name = 'payment.payment'
    _description = 'Payment'

    student_id = fields.Many2one('student.student', string='Student', required=True)
    group_id = fields.Many2one('course.group', string='Group', required=True)
    amount = fields.Float(string='Amount', required=True)
    date = fields.Date(string='Payment Date', required=True, default=fields.Date.context_today)
    status = fields.Selection([('pending', 'Pending'), ('completed', 'Completed')], string='Status', default='pending')
    description = fields.Text(string='Description')
