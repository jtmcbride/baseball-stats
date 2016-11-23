from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
import json
from .serializers import Serializer
import pdb


from .models import Player, Teams

# player_serializer = PlayerSerializer()

# Create your views here.

def index(request):
	pass

def player(request, player_id):
	player = Player.objects.filter(playerid=player_id)
	response = {"status": 200, "player": player.values()[0], "careerStats": player[0].career_batting()}
	return JsonResponse(response)


def players(request):
	order = "namelast"
	offset = 25
	if 'order' in request.GET:
		order = request.GET['order']
	if 'p' in request.GET:
		offset = int(request.GET['p']) * 25
	players = Player.objects.all().order_by("-" + order)[offset-25:offset]
	response = {"status": 200, "players": list(players.values()), "currentPage": offset/25}
	return JsonResponse(response)

def team(request, team_id):
	team = Teams.objects.filter(pk_teamid=team_id.upper())
	player_stats = team[0].player_batting_stats.all().values()
	response = {
		"status": 200,
		"team": list(team.values())[0],
		"player_batting_stats":  list(player_stats)
	}
	return JsonResponse(response)

def teams(request):
	order = "yearid"
	offset = 25
	if 'order' in request.GET:
		order = request.GET['order']
	if 'year' in request.GET:
		year = request.GET['year']
		teams = Teams.objects.filter(yearid=year).order_by("-" + order)
		response = {"status": 200, "teams": list(teams.values())}
		return JsonResponse(response)
	if 'p' in request.GET:
		offset = int(request.GET['p']) * 25
	teams = Teams.objects.all().order_by("-" + order)[offset-25:offset]
	response = {"status": 200, "teams": list(teams.values()), "currentPage": offset/25}
	return JsonResponse(response)

def team(request, team_id):
	team = Teams.objects.filter(pk_teamid=team_id.upper())
	player_stats = team[0].player_batting_stats.all().values()
	response = {
		"status": 200,
		"team": list(team.values())[0],
		"player_batting_stats":  list(player_stats)
	}
	return JsonResponse(response)


def franchise(request, franch_id):
	teams = Teams.objects.filter(franchid=franch_id.upper()).values()
	response = {"status": 200, "teams": list(teams)}
	return JsonResponse(response)

