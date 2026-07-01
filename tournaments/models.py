from django.db import models
from teams.models import Team

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    is_active = models.BooleanField(default=True)

    teams = models.ManyToManyField(
        Team,
        related_name='tournaments'
    )

    def __str__(self):
        return self.name