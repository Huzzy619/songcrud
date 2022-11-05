from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Artiste, Song
from .serializers import (ArtisteSerializer, SongSerializer,
                          UpdateSongSerializer)

# Create your views here.


class ArtisteView (APIView):
    # To list all artist
    def get(self, request, *args, **kwargs):
        artistes = Artiste.objects.all()
        serializer = ArtisteSerializer(artistes, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'PUT':
            return UpdateSongSerializer
        return SongSerializer

# class test (APIView):
#     def post(self, request, *args, **kwargs):
#         print(request.data)

#         return Response ('ok')
