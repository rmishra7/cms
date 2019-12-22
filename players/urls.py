
from django.conf.urls import url

from players import apis

urlpatterns = [
    url(r'^$', apis.TeamsPlayerListApi.as_view(), name="api_players_queryset"),
]
