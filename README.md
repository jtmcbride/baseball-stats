# BaseballDB

BaseballDB is an API that allows you to get all your baseball statistics in convenient JSON format. BaseballDB runs on a Django backend with a mySQL database. The baseb URL is https://baseball-db.herokuapp.com/api/. All data is returned in JSON format.

## Endpoints

### /players

Parameters:

* p: Page number, default: 1
* order: field to order results by, default: namelast

Returns

### /player/:playerid

Returns player personal data as well as statistics by year.

### /player/search

Parameters:

* q: query, required

Return players by matcing of query to first or last name.


### /team

Parameters:

* q: query, required



