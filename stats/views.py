from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
import json
from .serializers import Serializer
import pdb


from .models import Player, Teams

# player_serializer = PlayerSerializer()

# Create your views here.
mimetype = 'application/json'

def index(request):
	pass

def players(request):
	# pdb.set_trace()
	player_json = Serializer.serialize(Player.objects.filter(namelast="Bonds"))
	return HttpResponse(player_json, mimetype)

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
	team = Teams.objects.get(pk_teamid=team_id.upper())
	player_stats = Serializer.serialize(team.player_batting_stats.all())
	team_json = Serializer.serialize([team])
	response = {
		"status": 200,
		"team": json.loads(team_json),
		"player_batting_stats":  json.loads(player_stats)
	}
	# pdb.set_trace()
	return JsonResponse(response)


def franchise(request, franch_id):
	teams = Teams.objects.filter(franchid=franch_id.upper()).values()
	# pdb.set_trace()
	response = {"status": 200, "teams": list(teams)}
	return JsonResponse(response)

