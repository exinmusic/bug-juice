from django.urls import path
from .import views

urlpatterns = [
    path('submit', views.submit),
    path('tickets', views.tickets),
    path('bugs', views.bugs)
]