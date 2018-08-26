from django.urls import path


from . import views


urlpatterns = [
    path('', views.result, name='result'),
    # path(r'other', views.other, name='other')
]