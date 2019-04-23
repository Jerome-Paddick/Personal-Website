from django.contrib import admin

from .models import NetworkMapNodes, NetworkMapConnections, CountryMap

admin.site.register(NetworkMapNodes)
admin.site.register(NetworkMapConnections)
admin.site.register(CountryMap)