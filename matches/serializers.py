
from rest_framework import serializers

from .models import Match
from teams.serializers import TeamsSerializer


class MatchSerializer(serializers.ModelSerializer):

    team1 = serializers.SerializerMethodField(source="get_team1")
    team2 = serializers.SerializerMethodField(source="get_team2")
    winner = serializers.SerializerMethodField(source="get_winner")

    def get_team1(self, obj):
        if obj.team1 is not None:
            return TeamsSerializer(obj.team1).data
        return None

    def get_team2(self, obj):
        if obj.team2 is not None:
            return TeamsSerializer(obj.team2).data
        return None

    def get_winner(self, obj):
        if obj.winner is not None:
            return TeamsSerializer(obj.winner).data
        return None

    class Meta:
        model = Match
        fields = '__all__'
