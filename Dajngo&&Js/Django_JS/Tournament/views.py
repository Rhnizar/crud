from django.shortcuts import render
from django.http import HttpResponse
from .models import Player, Tournament, PlayerTournament

# Create your views here.

def create(request):
    # Create a player and a tournament
    player = Player.objects.create(name='John Doe')
    tournament = Tournament.objects.create(name='Summer Cup')
    # Add the player to the tournament using the intermediary model
    PlayerTournament.objects.create(player=player, tournament=tournament)
    return (HttpResponse("models is created"))

def check_relationship(request):
    # Verify the relationship
    player = Player.objects.get(name='John Doe')
    tournament = Tournament.objects.get(name='Summer Cup')
    print(tournament.players.all())  # Should list John Doe
    print(player.tournaments.all())  # Should list Summer Cup
    print(Player.objects.all)  # print all players

    return (HttpResponse("test"))



