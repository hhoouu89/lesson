from super_web_framework.templator import render
from super_web_framework.views.shared.shared import *
from patterns.structural_patterns import *


@AppRoute(routes=routes, url='/create-course/')
class CreateCourse:
    category_id = -1

    @Debug(name='CreateCourse')
    def __call__(self, request):
        if request['method'] == 'POST':
            data = request['data']
            name = data['name']
            name = site.decode_value(name)
            category = None
            if self.category_id != -1:
                category = site.find_category_by_id(int(self.category_id))

                course = site.create_course('record', name, category)
                course.observers.append(email_notifier)
                course.observers.append(sms_notifier)
                site.courses.append(course)
            return '200 OK', render('course_list.html', objects_list=category.courses,
                                    name=category.name, id=category.id)
        else:
            self.category_id = int(request['request_params']['id'])
            category = site.find_category_by_id(int(self.category_id))

            return '200 OK', render('create_course.html', name=category.name, id=category.id)
