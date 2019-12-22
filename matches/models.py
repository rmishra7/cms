from django.db import models
from django.db.models.query import QuerySet
from django.utils.translation import ugettext_lazy as _

from teams.models import Team


class MatchMixin(object):
    pass


class MatchQuerySet(QuerySet, MatchMixin):
    pass


class MatchManager(models.Manager, MatchMixin):

    def get_queryset(self):
        return MatchQuerySet(self.model, using=self._db)


class Match(models.Model):
    """
    model to store matche details played between teams
    """
    team1 = models.ForeignKey(Team, related_name=_("team1_metch"), on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name=_("team2_match"), on_delete=models.CASCADE)
    date = models.DateField(_("match date"))
    winning_stat = models.CharField(_("Winning stats"), max_length=64, default='')
    winner = models.ForeignKey(Team, related_name=_("winner_team"), null=True, on_delete=models.CASCADE)

    objects = MatchManager()

    class Meta:
        verbose_name = "Match"
        verbose_name_plural = "Matchs"
        app_label = "matches"
        ordering = ("-date", )

    def __unicode__(self):
        return "%s" % (self.team1.name + " vs " + self.team2.name)
