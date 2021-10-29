from currency.views import contact_list, rate_list

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),

    path('rate/list/', rate_list),
    path('contact/list/', contact_list)
    ]
