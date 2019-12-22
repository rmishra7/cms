
from django.conf.urls import url

from points import apis


urlpatterns = [
    url(r'^$', apis.PointsTableApi.as_view(), name="api_points_table")
]
