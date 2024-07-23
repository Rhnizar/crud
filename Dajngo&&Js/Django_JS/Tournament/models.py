from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    players = models.ManyToManyField(Player, through='PlayerTournament', related_name='tournaments')
    def __str__(self):
        return self.name

class PlayerTournament(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)
    # def __str__(self):
    #     return self.date_joined