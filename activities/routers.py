from django.urls import path, include
from rest_framework.routers import DefaultRouter
from activities.views import ActivityViewSets

router = DefaultRouter()

router.register(r'activity',ActivityViewSets)

urlpatterns = router.urls