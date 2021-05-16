from super_web_framework.views.shared.shared import *
from patterns.structural_patterns import *


@AppRoute(routes=routes, url='/student-list/')
class StudentListView(ListView):
    queryset = site.students
    template_name = 'student_list.html'
