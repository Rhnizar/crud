from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import  Tournament, Stage, Player
# from .models import Player, Tournament, PlayerTournament

# Create your views here.

def index(request):
    return(HttpResponse("Test Tournament "))


def create_tournament(request):
    if request.method == 'POST':
        # Assume request.POST contains the necessary data
        tournament = Tournament.objects.create(
            name=request.POST['name'],
            start_date=request.POST['start_date'],
            end_date=request.POST['end_date'],
            num_players=request.POST['num_players']
        )

        # Create stages
        stages_data = request.POST.getlist('stages')
        for stage_data in stages_data:
            Stage.objects.create(
                tournament=tournament,
                stage_type=stage_data['stage_type'],
                date=stage_data['date'],
                ready_to_play=stage_data.get('ready_to_play', False)
            )

        return JsonResponse({'status': 'success'})

# Example of updating a tournament and its stages via a view or API

def update_tournament(request, tournament_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)

    if request.method == 'POST':
        tournament.name = request.POST['name']
        tournament.start_date = request.POST['start_date']
        tournament.end_date = request.POST['end_date']
        tournament.num_players = request.POST['num_players']
        tournament.save()

        # Update stages
        stages_data = request.POST.getlist('stages')
        for stage_data in stages_data:
            stage = get_object_or_404(Stage, id=stage_data['id'])
            stage.stage_type = stage_data['stage_type']
            stage.date = stage_data['date']
            stage.ready_to_play = stage_data.get('ready_to_play', False)
            stage.save()

        return JsonResponse({'status': 'success'})

# def create(request):
#     # Create a player and a tournament
#     player = Player.objects.create(name='John Doe')
#     tournament = Tournament.objects.create(name='Summer Cup')
#     # Add the player to the tournament using the intermediary model
#     PlayerTournament.objects.create(player=player, tournament=tournament)
#     return (HttpResponse("models is created"))

# def check_relationship(request):
#     # Verify the relationship
#     player = Player.objects.get(name='John Doe')
#     tournament = Tournament.objects.get(name='Summer Cup')
#     print(tournament.players.all())  # Should list John Doe
#     print(player.tournaments.all())  # Should list Summer Cup
#     print(Player.objects.all)  # print all players

#     return (HttpResponse("test"))



