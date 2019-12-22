
from rest_framework import generics, serializers

from .models import Match
from .serializers import MatchSerializer


class MatchListApi(generics.ListAPIView):
    """
    match queryset/list API
    """
    model = Match
    serializer_class = MatchSerializer

    def get_queryset(self):
        queryset = self.model.objects.all()
        kwargs = {}
        for key, vals in self.request.GET.lists():
            if key not in [x.name for x in self.model._meta.fields] and key not in ['page_size', 'page', 'ordering', 'teams']:
                raise serializers.ValidationError("Invalid query param passed: " + str(key))
            for v in vals:
                kwargs[key] = v
        if 'page_size' in kwargs:
            kwargs.pop('page_size')
        if 'page' in kwargs:
            kwargs.pop('page')
        if 'ordering' in kwargs:
            kwargs.pop('ordering')
        if 'teams' in kwargs:
            kwargs['team1__in'] = kwargs['teams'].split(',')
            kwargs['team2__in'] = kwargs['teams'].split(',')
            kwargs.pop('teams')
        print (kwargs)
        queryset = queryset.filter(**kwargs)
        if self.request.query_params.get('ordering', None) not in [None, ""]:
            ordering = self.request.query_params.get('ordering', None)
            return queryset.order_by(ordering)
        return queryset
