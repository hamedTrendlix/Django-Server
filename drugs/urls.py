from django.urls import path

from . import views

urlpatterns = [
    path('', views.getDrug, name='getDrug'),
]