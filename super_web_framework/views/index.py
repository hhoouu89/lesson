from super_web_framework.templator import render
from super_web_framework.views.shared.shared import *
from patterns.structural_patterns import *


@AppRoute(routes=routes, url='/')  # todo: add url='/index/'
class Index:
    @Debug(name='Index')
    def __call__(self, request):
        return '200 OK', render('index.html', objects_list=site.categories)
