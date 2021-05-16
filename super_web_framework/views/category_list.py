from super_web_framework.templator import render
from patterns.structural_patterns import *
from super_web_framework.views.shared.shared import *


@AppRoute(routes=routes, url='/category-list/')
class CategoryList:
    @Debug(name='CategoryList')
    def __call__(self, request):
        logger.log('Список категорий')
        return '200 OK', render('category_list.html', objects_list=site.categories)