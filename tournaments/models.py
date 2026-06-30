from django.db.models.deletion import models
from teams.models import Team

class Tournament(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    teams = models.ManyToManyField(Team,related_name='tournaments')
    def __str__(self):
        return self.title