
from django.shortcuts import get_object_or_404

from rest_framework import generics, response, status, serializers

from .models import Team
from .serializers import TeamsSerializer, TeamsDetailSerializer


class TeamsListApi(generics.ListAPIView):
    """
    api to return list of teams
    """
    model = Team
    serializer_class = TeamsSerializer

    def get_queryset(self):
        queryset = self.model.objects.all()
        kwargs = {}
        for key, vals in self.request.GET.lists():
            if key not in [x.name for x in self.model._meta.fields] and key not in ['page_size', 'page', 'ordering']:
                raise serializers.ValidationError("Invalid query param passed: " + str(key))
            for v in vals:
                kwargs[key] = v
        if 'page_size' in kwargs:
            kwargs.pop('page_size')
        if 'page' in kwargs:
            kwargs.pop('page')
        if 'ordering' in kwargs:
            kwargs.pop('ordering')
        queryset = queryset.filter(**kwargs)
        if self.request.query_params.get('ordering', None) not in [None, ""]:
            ordering = self.request.query_params.get('ordering', None)
            return queryset.order_by(ordering)
        return queryset


class TeamsDetailApi(generics.RetrieveAPIView):
    """
    api to return teams detail
    """
    model = Team
    serializer_class = TeamsDetailSerializer
    lookup_url_kwarg = 'teams_id'

    def get_object(self):
        return get_object_or_404(self.model, id=self.kwargs[self.lookup_url_kwarg])

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
