from django.http import HttpResponse
from .models import NetworkMapNodes, NetworkMapConnections, CountryMap

def index(request):
    output = NetworkMapNodes.objects.order_by('-name')
    return HttpResponse(output)