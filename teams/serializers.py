
from rest_framework import serializers

from .models import Team


class TeamsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('id', 'name', 'logouri')


class TeamsDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        exclude = ('delete', )
