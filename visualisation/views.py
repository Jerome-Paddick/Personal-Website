from django.http import HttpResponse
from django.template import loader
from .models import NetworkMapNodes, NetworkMapConnections, CountryMap

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())