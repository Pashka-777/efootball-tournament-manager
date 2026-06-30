from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)

    logo = models.ImageField(
        upload_to='team_logos/',
        blank=True,
        null=True
    )

    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name