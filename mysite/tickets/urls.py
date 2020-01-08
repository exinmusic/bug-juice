from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('dash', views.dash),
    path('submit', views.submit),
    path('tickets', views.tickets),
    path('bugs', views.bugs),
    path('solutions', views.solutions)
]