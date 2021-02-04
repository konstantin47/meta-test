from rest_framework import serializers

from .models import Psychotherapist


class PsychotherapistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Psychotherapist
        fields = ['id']


class PsychotherapistDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Psychotherapist
        fields = ['data']
