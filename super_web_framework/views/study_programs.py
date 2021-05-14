from datetime import date
from super_web_framework.templator import render
from super_web_framework.views.shared.shared import site, logger


class StudyPrograms:
    def __call__(self, request):
        return '200 OK', render('study-programs.html', data=date.today())
