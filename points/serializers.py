
from rest_framework import serializers

from .models import PointTable
from teams.serializers import TeamsSerializer


class PointTableSerializer(serializers.ModelSerializer):

    team = TeamsSerializer()

    class Meta:
        model = PointTable
        fields = '__all__'
