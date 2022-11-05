from rest_framework import serializers

from .models import *


class ArtisteSerializer (serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = ['first_name', 'last_name']


class SongSerializer (serializers.ModelSerializer):
    artiste = ArtisteSerializer(read_only=True)

    class Meta:
        model = Song
        fields = ['id', 'title', 'date_released', 'likes', 'artiste']


class UpdateSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['title', 'date_released']
