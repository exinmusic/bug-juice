from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('dashboard', views.dash),
    path('dashboard/tickets', views.tickets),
    path('submit', views.submit),
    path('bugs', views.bugs),
    path('solutions', views.solutions)
]