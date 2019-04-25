from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cv', views.cv, name='cv'),
    path('about', views.about, name='about'),
    path('visualisation', include('visualisation.urls')),
    path('admin/', admin.site.urls),

]

from django.views.generic import TemplateView
# from django.views.generic import RedirectView
# # redirects main page to visualisations
# urlpatterns += [
#     path('', RedirectView.as_view(url='/visualisation/', permanent=True)),
# ]