from odoo import fields, models, api
from odoo.exceptions import ValidationError


class SchoolGrades(models.Model):
    _name = 'school.grades'
    _rec_name = 'grade'
    _description = 'School Grades'

    grade = fields.Char(string='Grade', required=True)
    tuition = fields.Integer(string='Tuition Fees', required=True)
    color = fields.Integer(string='Color')


class SchoolSubjects(models.Model):
    _name = 'school.subjects'
    _rec_name = 'subject'
    _description = 'School Subjects'

    subject = fields.Char(string='Subject Name',
                          required=True)


class GradeIntervals(models.Model):
    _name = 'grade.intervals'
    _rec_name = 'letter_grade'
    _description = 'Grading Intervals'

    bottom_limit = fields.Integer(string='From', required=True)
    top_limit = fields.Integer(string='To', required=True)
    letter_grade = fields.Char(string='Grade', required=True)
    numerical_grade = fields.Float(string='Numerical Value', required=True)

    @api.constrains('bottom_limit', 'top_limit')
    def _check_bottom_top_limits(self):
        for interval in self:
            if interval.bottom_limit > interval.top_limit:
                raise ValidationError("Bottom limit must be less than or equal to top limit.")


class AcademicYear(models.Model):
    _name = 'academic.years'
    _rec_name = 'academic_year'
    _description = 'Academic Year'

    academic_year = fields.Char(string='Academic Year')
    default_val = fields.Boolean(string='Active')

    @api.constrains('default_val')
    def only_one_default(self):
        all_values = self.env['academic.years'].search([('default_val','=',True)])
        if len(all_values) >= 2:
            raise ValidationError('There can only be one academic year default at a time!')
        elif len(all_values) == 0:
            raise ValidationError('There needs to be a default year chosen!')


class AllMonths(models.Model):
    _name = 'all.months'
    _rec_name = 'month'
    _description = 'All Months'

    month = fields.Char(string='Month')


class AcademicQuarters(models.Model):
    _name = 'academic.quarters'
    _rec_name = 'academic_quarter'
    _description = 'Academic Quarters'

    academic_quarter = fields.Char(string='Academic Quarter')


class LMSCalendarEventType(models.Model):
    _name = 'lms.calendar.event.type'
    _rec_name = 'name'
    _description = 'Calendar Event Types'

    name = fields.Char(string='Event')
    color = fields.Integer(string='Color')
