from django.urls import path
from .import views

urlpatterns = [
    path('<rid>', views.report),
    path('manage/<rid>', views.manage),
    path('comment/<rid>', views.comment),
    path('todo/<rid>', views.todo)
]