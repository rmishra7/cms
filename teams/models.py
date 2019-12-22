from django.db import models
from django.db.models.query import QuerySet
from django.utils.translation import ugettext_lazy as _


class TeamMixin(object):
    pass


class TeamQuerySet(QuerySet, TeamMixin):
    pass


class TeamManager(models.Manager, TeamMixin):

    def get_queryset(self):
        return TeamQuerySet(self.model, using=self._db).filter(delete=False)


class Team(models.Model):
    """
    model to store team records
    """
    name = models.CharField(_("Team Name"), max_length=64)
    logouri = models.URLField(_("Team Logo URI"))
    club_state = models.CharField(_("Club State"), max_length=32)
    delete = models.BooleanField(default=False)

    objects = TeamManager()

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"
        app_label = "teams"
        ordering = ("-name", )

    def __unicode__(self):
        return "%s" % (self.name)
