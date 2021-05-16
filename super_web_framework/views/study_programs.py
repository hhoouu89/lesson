from datetime import date
from super_web_framework.templator import render
from super_web_framework.views.shared.shared import *
from patterns.structural_patterns import *


@AppRoute(routes=routes, url='/study_programs/')
class StudyPrograms:
    @Debug(name='StudyPrograms')
    def __call__(self, request):
        return '200 OK', render('study-programs.html', data=date.today())
