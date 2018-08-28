from django.urls import path


from . import views


urlpatterns = [
    path(r'result', views.result, name='result'),
    path(r'clinic', views.clinic, name='clinic'),
    path(r'map', views.map, name='map'),
]