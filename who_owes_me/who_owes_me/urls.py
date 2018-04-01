from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
# from django.conf.urls import url
# from .settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('debt_manager/', include('debt_manager.urls')),
    path('', RedirectView.as_view(url='/debt_manager/', permanent=True)),
    # url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT.replace('\\','/')}, name='media'),
]
