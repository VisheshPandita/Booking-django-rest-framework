from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permission import IsAuthenticated

from .models import Event
from .serialzers import EventSerializer


class GetEvents(APIView):

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
