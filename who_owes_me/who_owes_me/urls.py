from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('debt_manager/', include('debt_manager.urls')),
    path('', RedirectView.as_view(url='/debt_manager/', permanent=True)),
]
