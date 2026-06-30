from django.db import models
from teams.models import Team
from tournaments.models import Tournament

class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_team')

    home_score = models.PositiveIntegerField(default=0)
    away_score = models.PositiveIntegerField(default=0)
    match_data =models.DateTimeField()

    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"
