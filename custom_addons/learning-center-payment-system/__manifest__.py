{
    'name': 'Payment Automation for Educational Center',
    'version': '1.0',
    'summary': 'Automates payment management in an educational center',
    'description': """
        Manage and automate the payment process for students and teachers in an educational center.
        Includes course, group, teacher, student, and payment management.
    """,
    'author': 'Asadbek',
    'sequence': 0,
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'security/payment_automation_security.xml',
        'security/ir.model.access.csv',
        'views/course_view.xml',
        'views/group_view.xml',
        'views/teacher_veiw.xml',
        'views/student_view.xml',
        'views/payment_view.xml',
        'views/teacher_payment_views.xml',
    ],
    'installable': True,
    'application': True,
}
