from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def cv(request):
    template = loader.get_template('cv.html')
    return HttpResponse(template.render())