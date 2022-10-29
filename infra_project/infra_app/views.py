from django.http import HttpResponse


def index(request):
    return HttpResponse('i want to be free!!!')


def second_page(request):
    return HttpResponse('А это вторая страница')
