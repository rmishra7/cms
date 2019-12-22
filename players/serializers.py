
from rest_framework import serializers

from .models import Player


class TeamsPlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ('id', 'first_name', 'last_name', 'imageuri')
