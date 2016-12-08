# BaseballDB

BaseballDB is an API that allows you to get all your baseball statistics in convenient JSON format. BaseballDB runs on a Django backend with a Postgres database all running on AWS EC2. The base URL is http://baseballdb.online/api/. All data is returned in JSON format.

An example application utilizing the API can be found [here](http://baseballdb.online/app/index.html). [Github](https://github.com/jtmcbride/baseball-graphs).

## Endpoints

### /players

Parameters:

* p: Page number, default: 1
* order: field to order results by, default: namelast

Returns list of players.

### /player/:playerid

Returns player personal data as well as statistics by year.

### /player/search

Parameters:

* q: query, required

Return players by matcing of query to first or last name.


### /teams

Parameters:

* p: Page number, default: 1
* order: field to order results by, default: year
* year: year to return teams from, defualt: none

Returns list of players.

### /team/:teamid

Returns team data. Teamid points to a specific team for a specific year.


### /franchise/:franchid

Returns all teams from a given franchise.


### /baberuth/:playerid

Returns distance from Babe Ruth for given player and information about the links in ordered lists.




