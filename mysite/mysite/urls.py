from django.contrib import admin
from django.urls import path, include

handler403 = 'tickets.views.permission_denied_view'
handler404 = 'tickets.views.not_found_view'

urlpatterns = [
    path('', include('tickets.urls')),
    path('users/', include('users.urls')),
    path('reports/', include('reports.urls')),
    path('admin/', admin.site.urls),
]
