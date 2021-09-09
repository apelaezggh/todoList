from django.urls import path
from activities.api import activity_api_view, activity_detail_api_view

urlpatterns = [
    path('activity/', activity_api_view, name = 'activity_api'),
    path('activity/<int:pk>/', activity_detail_api_view, name= 'activity_detail_api_view')
]