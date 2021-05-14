from datetime import date
from super_web_framework.templator import render
from super_web_framework.views.shared.shared import site, logger


class CreateCategory:

    def __call__(self, request):
        if request['method'] == 'POST':
            print(request)
            post_request_data = request['post_request_data']
            data = request['data']
            name = post_request_data['name']
            name = site.decode_value(name)
            category_id = data.get('category_id')
            category = None
            if category_id:
                category = site.find_category_by_id(int(category_id))
            new_category = site.create_category(name, category)
            site.categories.append(new_category)
            return '200 OK', render('index.html', objects_list=site.categories)
        else:
            categories = site.categories
            return '200 OK', render('create_category.html', categories=categories)
