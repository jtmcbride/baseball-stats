## Baseball Stats

### Background

This app will create an api for baseball statistics that can be used for any number of different apps. I will also include a small frontend app along with it that will allow data visualization through the api.

### Functionality & MVP

With this app, users will be able to:

- [ ] Query the api directly for JSON formatted stats,
- [ ] Stats can queried by a variety of constraints such as year, team, player, etc.
- [ ] The frontend app will allow users to generate graphs of certain statistics

### Technologies & Technical Challenges

This app will be implemented using python and the Django framework with a postgres database. The database will be built from the Sea Lahman baseball database. The frontend will be built using React and D3.js

There will be models for:
-Teams
-Players
-Stats

### Implementation Timeline

**Day 1**: Setup the database and the django models

- A django app up and running
- A database completely setup with all data

**Day 2**: Api routes setup to correctly query the databse and return json formatted data

- routes for teams and players

**Day 3**: Set up frontend application

- get working ajax calls to the backend
- begin working on D3 graphs

**Day 4**: Get basic graph working on frontend and style it too
