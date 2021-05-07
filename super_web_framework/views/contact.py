from super_web_framework.templator import render


class Contact:
    def __call__(self, request):
        return '200 OK', render('contact.html', data=request.get('data', None))
