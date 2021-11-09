from currency.views import (
    ContactUsCreateView, RateCreateView, RateDeleteView,
    RateDetailsView, RateListView, RateUpdateView,
    SourceCreateView, SourceDeleteView, SourceDetailsView,
    SourceListView, SourceUpdateView,
)


from django.urls import path

app_name = 'currency'

urlpatterns = [
    path('rate/list/', RateListView.as_view(), name='rate-list'),
    path('rate/create/', RateCreateView.as_view(), name='rate-create'),
    path('rate/update/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('rate/details/<int:pk>/', RateDetailsView.as_view(), name='rate-details'),
    path('rate/delete/<int:pk>/', RateDeleteView.as_view(), name='rate-delete'),
    path('source/list/', SourceListView.as_view(), name='source-list'),
    path('source/create/', SourceCreateView.as_view(), name='source-create'),
    path('source/update/<int:pk>/', SourceUpdateView.as_view(), name='source-update'),
    path('source/details/<int:pk>/', SourceDetailsView.as_view(), name='source-details'),
    path('source/delete/<int:pk>/', SourceDeleteView.as_view(), name='source-delete'),
    path('contactus/create/', ContactUsCreateView.as_view(), name='contactus-create'),
]
