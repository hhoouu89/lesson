from datetime import date
from super_web_framework.templator import render
from super_web_framework.views.shared.shared import site, logger


class CoursesList:
    def __call__(self, request):
        logger.log('Список курсов')
        try:
            category_id = int(request['request_params']['id'])
            category = site.find_category_by_id(category_id)
            return '200 OK', render('course_list.html', objects_list=category.courses,
                                    name=category.name, id=category.id)
        except KeyError:
            return '200 OK', 'No courses have been added yet'
