from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from django.db.models.functions import Concat

import json
import pdb

from .models import Player, Teams

def index(request):
	HttpResponse("hello")


def player(request, player_id):
	player = Player.objects.prefetch_related('batting_stats').filter(playerid=player_id)
	response = {
		"status": 200,
		"player": player.values()[0],
		# "careerStats": player[0].career_batting(),
		"batting_stats": list(player[0].batting_stats.values())
	}
	return JsonResponse(response)


def players(request):
	order = "namelast"
	offset = 25
	if 'order' in request.GET:
		order = request.GET['order']
	if 'p' in request.GET:
		offset = int(request.GET['p']) * 25
	players = Player.objects.all().order_by("-" + order)[offset-25:offset]
	response = {
		"status": 200,
		"players": list(players.values()),
		"currentPage": offset/25
	}
	return JsonResponse(response)


def player_search(request):
	if 'q' not in request.GET:
		return JsonResponse({"data": "requires query(q)"})
	else:
		q = request.GET['q']
		players = Player.objects.annotate(fullname=Concat('namefirst', 'namelast')).filter(Q(fullname__icontains=q))[:20].values()
		return JsonResponse({'players': list(players)})


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
	response = {
		"status": 200,
		"teams": list(teams.values()), 
		"currentPage": offset/25
	}
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
	response = {
		"status": 200, 
		"teams": list(teams)
	}
	return JsonResponse(response)


def babe_ruth(request, player_id):
	player = Player.objects.get(playerid=player_id)
	answer = player.babe_ruth_distance()
	return JsonResponse({"result": answer})
