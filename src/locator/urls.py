from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('position/<str:lat>/<str:long>', views.index, name='position'),
    path('logPassW', views.logPassW)
]