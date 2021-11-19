import debug_toolbar

from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from currency.views import ProfileView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('__debug__/', include(debug_toolbar.urls)),

    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('auth/', include('django.contrib.auth.urls')),
    path('currency/', include('currency.urls')),
    path('silk/', include('silk.urls', namespace='silk')),
    ]
