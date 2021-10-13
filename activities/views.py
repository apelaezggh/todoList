from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics

from activities.models import Activity
from activities.serializers import ActivitySerializer

class ActivityViewSets(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


# Create your views here.
