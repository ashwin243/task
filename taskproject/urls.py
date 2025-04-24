from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # 👈 make sure this is imported

urlpatterns = [
    path('admin/', admin.site.urls),                 # Admin panel
    path('api/', include('tasks.urls')),             # API route
    path('', RedirectView.as_view(url='/api/tasks/', permanent=False)),  # 👈 Redirect root URL
]
