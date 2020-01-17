from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('dashboard', views.dash),
    path('dashboard/tickets', views.tickets),
    path('dashboard/solutions', views.solutions),
    path('submit', views.submit)
]