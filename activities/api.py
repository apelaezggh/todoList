from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from activities.models import Activity
from activities.serializers import ActivitySerializer

@api_view(['GET','POST'])
def activity_api_view(request):

    if request.method == 'GET':
        activity = Activity.objects.all()
        activity_serializer = ActivitySerializer(activity, many = True)
        return Response(activity_serializer.data, status = status.HTTP_200_OK)

    elif request.method == 'POST':
        activity_serializer = ActivitySerializer(data = request.data)
        if activity_serializer.is_valid():
            activity_serializer.save()
            return Response(activity_serializer.data, status = status.HTTP_201_CREATED)

        return Response({'message':'Incorrect innformation'}, status = status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT','DELETE'])
def activity_detail_api_view(request,pk=None):

    activity = Activity.objects.filter(id = pk).first()

    if activity:

        if request.method == 'GET':
            activity_serializer = ActivitySerializer(activity)
            return Response(activity_serializer.data, status = status.HTTP_200_OK)

        elif request.method == 'PUT':
            activity_serializer = ActivitySerializer(activity, data = request.data)
            if activity_serializer.is_valid():
                activity_serializer.save()
                return Response(activity_serializer.data, status = status.HTTP_200_OK)
            return Response({'message':'Incorrect innformation'}, status = status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            activity.delete()
            return Response({'message':'User deleted'}, status = status.HTTP_200_OK)

    return Response({'message':'Do not find user'}, status = status.HTTP_400_BAD_REQUEST)




