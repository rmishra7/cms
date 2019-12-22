from django.db import models
from django.db.models.query import QuerySet
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator

from teams.models import Team


class PlayerMixin(object):
    pass


class PlayerQuerySet(QuerySet, PlayerMixin):
    pass


class PlayerManager(models.Manager, PlayerMixin):

    def get_queryset(self):
        return PlayerQuerySet(self.model, using=self._db).filter(delete=False)


class Player(models.Model):
    """
    model to store player records
    """
    team = models.ForeignKey(Team, related_name=_("team_player"), on_delete=models.CASCADE)
    first_name = models.CharField(_("Player First Name"), max_length=64)
    last_name = models.CharField(_("Player Last Name"), max_length=64)
    imageuri = models.URLField(_("Player Image URI"))
    jersey_no = models.IntegerField(_("Jersey Number"), validators=[MinValueValidator(0), ])
    country = models.CharField(_("Player Country"), max_length=24)
    matches = models.IntegerField(_("No. of Matches Played"))
    run = models.IntegerField(_("Player's Run"))
    highest_score = models.IntegerField(_("Highest Score"))
    halfcentury = models.IntegerField(_("Half Century"))
    century = models.IntegerField(_("Century"))
    delete = models.BooleanField(default=False)

    objects = PlayerManager()

    class Meta:
        verbose_name = "Player"
        verbose_name_plural = "Players"
        app_label = "players"
        ordering = ("-first_name", )

    def __unicode__(self):
        return "%s" % (self._get_full_name())

    def _get_full_name(self):
        return self.first_name + " " + self.last_name
