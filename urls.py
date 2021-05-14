from datetime import date
from super_web_framework.views.index import Index
from super_web_framework.views.about import About
from super_web_framework.views.contact import Contact
from super_web_framework.views.study_programs import StudyPrograms
from super_web_framework.views.courses_list import CoursesList
from super_web_framework.views.create_course import CreateCourse
from super_web_framework.views.create_category import CreateCategory
from super_web_framework.views.category_list import CategoryList
from super_web_framework.views.copy_course import CopyCourse


def front_layer_1(request):
    request['date'] = date.today()


def front_layer_2(request):
    request['key'] = 'key'


fronts = [front_layer_1, front_layer_2]

routes = {
    '/': Index(),
    '/index/': Index(),
    '/about/': About(),
    '/contact/': Contact(),
    '/study_programs/': StudyPrograms(),
    '/courses-list/': CoursesList(),
    '/create-course/': CreateCourse(),
    '/create-category/': CreateCategory(),
    '/category-list/': CategoryList(),
    '/copy-course/': CopyCourse()
}
