from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.db import connection
from django.db.models import Q
from django.db.models.functions import Concat


from .models import Player, Teams

from .ruth_tree import tree

def index(request):
	return render(request, "index.html")


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
	if "id" in request.GET:
		team = Teams.objects.prefetch_related("player_batting_stats__playerid").filter(id=int(request.GET["id"]))
		response = {"team": list(team.values())[0]}
		players = []
		for player in team[0].player_batting_stats.all():
			players.append(player.playerid.namefirst + " " + player.playerid.namelast)
		response["players"] = players
		return JsonResponse(response)
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

def babe_ruth_tree(request):
	return JsonResponse(tree)


def teammates(request):
	if 'player1' in request.GET and 'player2' in request.GET:
		playerid1 = request.GET['player1']
		playerid2 = request.GET['player2']
	else:
		return JsonResponse({
				"status": 422,
				"error": "invalid parameters"
			})
	cursor = connection.cursor()
	cursor.execute("""
					SELECT 
						fk_teamid 
					FROM 
						batting AS b1
					JOIN
						batting AS b2
					ON
						b1.fk_teamid = b2.fk_teamid
					WHERE
						b1.playerid = %s AND
						b2.playerid = %s
					""", [playerid1, playerid2])
	rows = cursor.fetchall()
	return JsonResponse({
				"status": 200,
				"teams": list(rows)
			})


