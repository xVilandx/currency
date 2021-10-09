from currency.views import rate_list

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),

    path('rate/list/', rate_list)
    ]
