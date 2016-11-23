from __future__ import unicode_literals

from django.db import models
from django.db.models import Sum

# Create your models here.
class BabeRuthNumbers(models.Model):
    player_id = models.CharField(max_length=10)
    team_id = models.CharField(unique=True, max_length=10)
    distance = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'babe_ruth_numbers'


class Batting(models.Model):
    playerid = models.ForeignKey('Player', models.DO_NOTHING, db_column='playerid', related_name="batting_stats", blank=True, null=True)
    yearid = models.IntegerField(blank=True, null=True)
    stint = models.IntegerField(blank=True, null=True)
    teamid = models.CharField(max_length=3, blank=True, null=True)
    lgid = models.CharField(max_length=2, blank=True, null=True)
    g = models.IntegerField(blank=True, null=True)
    ab = models.IntegerField(blank=True, null=True)
    r = models.IntegerField(blank=True, null=True)
    h = models.IntegerField(blank=True, null=True)
    dub = models.IntegerField(blank=True, null=True)
    trip = models.IntegerField(blank=True, null=True)
    hr = models.IntegerField(blank=True, null=True)
    rbi = models.IntegerField(blank=True, null=True)
    sb = models.IntegerField(blank=True, null=True)
    cs = models.IntegerField(blank=True, null=True)
    bb = models.IntegerField(blank=True, null=True)
    so = models.IntegerField(blank=True, null=True)
    ibb = models.IntegerField(blank=True, null=True)
    hbp = models.IntegerField(blank=True, null=True)
    sh = models.IntegerField(blank=True, null=True)
    sf = models.IntegerField(blank=True, null=True)
    gidp = models.IntegerField(blank=True, null=True)
    fk_teamid = models.ForeignKey('Teams', models.DO_NOTHING, db_column='fk_teamid', blank=True, null=True, related_name='player_batting_stats', to_field='pk_teamid')

    def __unicode__(self):
		return str(self.playerid) + ' (' + str(self.yearid) + ')'

    class Meta:
        managed = False
        db_table = 'batting'


class Player(models.Model):
    playerid = models.CharField(primary_key=True, max_length=9)
    birthyear = models.IntegerField(blank=True, null=True)
    birthmonth = models.IntegerField(blank=True, null=True)
    birthday = models.IntegerField(blank=True, null=True)
    birthcountry = models.TextField(blank=True, null=True)
    birthstate = models.TextField(blank=True, null=True)
    birthcity = models.TextField(blank=True, null=True)
    deathyear = models.IntegerField(blank=True, null=True)
    deathmonth = models.IntegerField(blank=True, null=True)
    deathday = models.IntegerField(blank=True, null=True)
    deathcountry = models.TextField(blank=True, null=True)
    deathstate = models.TextField(blank=True, null=True)
    deathcity = models.TextField(blank=True, null=True)
    namefirst = models.TextField(blank=True, null=True)
    namelast = models.TextField(blank=True, null=True)
    namegiven = models.TextField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    bats = models.CharField(max_length=1, blank=True, null=True)
    throws = models.CharField(max_length=1, blank=True, null=True)
    debut = models.DateField(blank=True, null=True)
    finalgame = models.DateField(blank=True, null=True)
    retroid = models.CharField(max_length=9, blank=True, null=True)
    bbrefid = models.CharField(max_length=9, blank=True, null=True)


    def career_batting(self):
        return self.batting_stats.aggregate(hr=Sum('hr'), h=Sum('h'),
                                            g=Sum('g'), ab=Sum('ab'),
                                            r=Sum('r'), bb=Sum('bb'),
                                            dub=Sum('dub'), trip=Sum('trip'),
                                            rbi=Sum('rbi'), sb=Sum('sb'),
                                            cs=Sum('cs'), ibb=Sum('ibb'),
                                            hbp=Sum('hbp'), sh=Sum('sh'),
                                            sf=Sum('sf'), gidp=Sum('gidp'))
    @staticmethod
    def all_players_with_batting(order_stat="hr"):
        return Player.objects.raw('''
            SELECT 
                master.namelast, 
                SUM(batting.hr) as hr,
                SUM(batting.h) as h,
                SUM(batting.bb) as bb,
                SUM(batting.ibb) as ibb,
                SUM(batting.dub) as dub,
                SUM(batting.trip) as trip,
                SUM(batting.g) as g,
                SUM(batting.ab) as ab,
                SUM(batting.r) as r
            FROM master 
                JOIN batting ON batting.playerid=master.playerid
            GROUP BY 
                master.playerid 
            ORDER BY hr DESC NULLS LAST
            LIMIT
                25''')

    def __unicode__(self):
		return self.namefirst + ' ' + self.namelast

    class Meta:
        managed = False
        db_table = 'master'


class SchemaMigrations(models.Model):
    version = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'schema_migrations'


class Teams(models.Model):
    yearid = models.IntegerField(blank=True, null=True)
    lgid = models.CharField(max_length=10, blank=True, null=True)
    teamid = models.CharField(max_length=10, blank=True, null=True)
    franchid = models.CharField(max_length=10, blank=True, null=True)
    divid = models.CharField(max_length=10, blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    g = models.IntegerField(blank=True, null=True)
    ghome = models.IntegerField(blank=True, null=True)
    w = models.IntegerField(blank=True, null=True)
    l = models.IntegerField(blank=True, null=True)
    divwin = models.CharField(max_length=10, blank=True, null=True)
    wcwin = models.CharField(max_length=10, blank=True, null=True)
    lgwin = models.CharField(max_length=10, blank=True, null=True)
    wswin = models.CharField(max_length=10, blank=True, null=True)
    r = models.IntegerField(blank=True, null=True)
    ab = models.IntegerField(blank=True, null=True)
    h = models.IntegerField(blank=True, null=True)
    dub = models.IntegerField(blank=True, null=True)
    trip = models.IntegerField(blank=True, null=True)
    hr = models.IntegerField(blank=True, null=True)
    bb = models.IntegerField(blank=True, null=True)
    so = models.IntegerField(blank=True, null=True)
    sb = models.IntegerField(blank=True, null=True)
    cs = models.IntegerField(blank=True, null=True)
    hbp = models.IntegerField(blank=True, null=True)
    sf = models.IntegerField(blank=True, null=True)
    ra = models.IntegerField(blank=True, null=True)
    er = models.IntegerField(blank=True, null=True)
    era = models.FloatField(blank=True, null=True)
    cg = models.IntegerField(blank=True, null=True)
    sho = models.IntegerField(blank=True, null=True)
    sv = models.IntegerField(blank=True, null=True)
    ipouts = models.IntegerField(blank=True, null=True)
    ha = models.IntegerField(blank=True, null=True)
    hra = models.IntegerField(blank=True, null=True)
    bba = models.IntegerField(blank=True, null=True)
    soa = models.IntegerField(blank=True, null=True)
    e = models.IntegerField(blank=True, null=True)
    dp = models.IntegerField(blank=True, null=True)
    fp = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=10, blank=True, null=True)
    park = models.CharField(max_length=10, blank=True, null=True)
    attendance = models.IntegerField(blank=True, null=True)
    bpf = models.IntegerField(blank=True, null=True)
    ppf = models.IntegerField(blank=True, null=True)
    teamidbr = models.CharField(max_length=10, blank=True, null=True)
    teamidlahman45 = models.CharField(max_length=10, blank=True, null=True)
    teamidretro = models.CharField(max_length=10, blank=True, null=True)
    pk_teamid = models.CharField(unique=True, max_length=20, blank=True, null=True)
    fk_teamid = models.CharField(max_length=20, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'teams'
