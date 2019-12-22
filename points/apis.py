
from rest_framework import generics, serializers

from .models import PointTable
from .serializers import PointTableSerializer


class PointsTableApi(generics.ListAPIView):
    """
    api to return list of teams
    """
    model = PointTable
    serializer_class = PointTableSerializer

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
