from super_web_framework.templator import render


class About:
    def __call__(self, request):
        return '200 OK', render('about.html', data=request.get('data', None))
