from django.conf.urls import url

from . import views

app_name = 'stats'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^api/player/([a-z0-9]{8,9})', views.player, name="player"),
	url(r'^api/players$', views.players, name="players"),
	url(r'^api/players/search', views.player_search, name="search"),
	url(r'^api/teams', views.teams, name="teams"),
	url(r'^api/team/([0-9]{4}[A-z]{3})', views.team, name="team"),
	# url(r'^api/team/([0-9]{4}[A-Z]{3})/players', views.team_players, name="team"),
	url(r'^api/franchise/([A-z]{3})', views.franchise, name="franchise"),
	url(r'^api/baberuth/([a-z0-9]{8,9})', views.babe_ruth, name='baberuth')
	# url(r'^generate/', views.generate),
	# url(r'^generate_player/', views.generate_player),
	# url(r'^players/([0-9]+)', views.players, name='players'),
	# url(r'^players/([a-z0-9]{8,9})', views.detail, name='detail'),
	# url(r'^get_players/', views.get_players, name='get_players')
]