from currency.views import (
    contact_list, delete_rate,
    delete_source, rate_create,
    rate_details, rate_list,
    source_create, source_details,
    source_list, update_rate,
    update_source,

)
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),

    path('rate/list/', rate_list),
    path('contact/list/', contact_list),
    path('rate/create/', rate_create),
    path('rate/update/<int:pk>/', update_rate),
    path('rate/delete/<int:pk>/', delete_rate),
    path('rate/details/<int:pk>/', rate_details),
    path('source/list/', source_list),
    path('source/create/', source_create),
    path('source/update/<int:pk>/', update_source),
    path('source/delete/<int:pk>/', delete_source),
    path('source/details/<int:pk>/', source_details),

    ]
