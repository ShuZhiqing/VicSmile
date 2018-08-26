from django.urls import path


from . import views


urlpatterns = [
    path('', views.diet, name='diet'),
    # path(r'other', views.other, name='other')
]