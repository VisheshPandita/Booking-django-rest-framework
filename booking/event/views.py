from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Event
from .serializers import EventSerializer


class GetAllEvents(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_obj(self):
        try:
            instance = Event.objects.all()
            return instance
        except ValueError:
            return Response(status.HTTP_404_NOT_FOUND)

    def get(self, request):
        instance = self.get_obj()
        instance = EventSerializer(instance, many=True)
        return Response(instance.data)


class GetEvent(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_obj(self, id):
        try:
            instance = Event.objects.get(id=id)
            return instance
        except ValueError:
            return Response(status.HTTP_404_NOT_FOUND)

    def get(self, request, slug):
        instance = self.get_obj(slug)
        instance = EventSerializer(instance)
        return Response(instance.data)


class PostEvent(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        instance = Event(host=request.user)
        instance = EventSerializer(instance, data=request.data)
        if instance.is_valid():
            event = instance.save()
            return Response(event.data, status=status.HTTP_201_CREATED)
        else:
            return Response(instance.errors, status=status.HTTP_400_BAD_REQUEST)


class BookForEvent(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_event(self, id):
        try:
            instance = Event.objects.get(id=id)
            return instance
        except ValueError:
            return Response(status.HTTP_404_NOT_FOUND)

    def post(self, request, slug):
        instance = self.get_event(slug)
        instance.audience.add(request.user)
        data = {}
        data['response'] = 'You are added to the show'
        return Response(data, status=status.HTTP_200_OK)