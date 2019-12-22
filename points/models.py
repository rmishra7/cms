from django.db import models
from django.db.models.query import QuerySet
from django.utils.translation import ugettext_lazy as _

from teams.models import Team


class PointTableMixin(object):
    pass


class PointTableQuerySet(QuerySet, PointTableMixin):
    pass


class PointTableManager(models.Manager, PointTableMixin):

    def get_queryset(self):
        return PointTableQuerySet(self.model, using=self._db)


class PointTable(models.Model):
    """
    team's Point
    """
    team = models.ForeignKey(Team, related_name=_("team_point"), on_delete=models.CASCADE)
    points = models.IntegerField(_("Team's Point"))

    class Meta:
        verbose_name = "PointTable"
        verbose_name_plural = "PointTable"
        app_label = "points"
        ordering = ("-points", )

    def __unicode__(self):
        return "%s" % (self.team.name)
