from . import views

from django.urls import path

urlpatterns = [
    path('', views.algo, name='algo')
]
