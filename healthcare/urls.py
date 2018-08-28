from django.urls import path
from . import views


urlpatterns = [
    path(r'system', views.system, name='system'),
    path(r'medicare', views.medicare, name='medicare'),
    path(r'rights', views.rights, name='rights'),
    path(r'translation', views.translation, name='translation'),
    path(r'insurance', views.insurance, name='insurance'),
    path(r'community', views.community, name='community'),
    path(r'healthcare', views.healthcare, name='healthcare'),
]