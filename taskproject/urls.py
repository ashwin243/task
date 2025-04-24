# taskproject/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),  # This should include the tasks app URLs
    path('', RedirectView.as_view(url='/admin/', permanent=False)),  # Optional: Redirect root to admin
]
