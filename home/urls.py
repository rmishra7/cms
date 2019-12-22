
from django.conf.urls import url
from django.views.generic import base


urlpatterns = [
    url(r'^$', base.TemplateView.as_view(template_name='home.html')),
    url(r'^team-dashboard/$', base.TemplateView.as_view(template_name='teams.html')),
    url(r'^player-dashboard/$', base.TemplateView.as_view(template_name='players.html')),
    url(r'^match-dashboard/$', base.TemplateView.as_view(template_name='match.html')),
    url(r'^point-table/$', base.TemplateView.as_view(template_name='points.html')),
]
