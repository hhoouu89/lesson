from super_web_framework.templator import render
from patterns.сreational_patterns import Engine
from super_web_framework.views.shared.shared import site, logger


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', objects_list=site.categories)
