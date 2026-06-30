from django.db import models
from teams.models import Team
class Player(models.Model):
    nickname = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE,related_name='players')
    def __str__(self):
        return self.nickname