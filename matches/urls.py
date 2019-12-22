
from django.conf.urls import url

from matches import apis


urlpatterns = [
    url(r'^$', apis.MatchListApi.as_view(), name="api_matches_queryset")
]
