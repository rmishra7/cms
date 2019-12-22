
from django.conf.urls import url, include

from teams import apis

urlpatterns = [
    url(r'^$', apis.TeamsListApi.as_view(), name="api_teams_queryset"),
    url(r'^ID:(?P<teams_id>\d+)/$', apis.TeamsDetailApi.as_view(), name="api_teams_details"),

    url(r'^ID:(?P<teams_id>\d+)/players/', include('players.urls'))
]
