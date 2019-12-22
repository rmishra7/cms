CMS: a sample project created with some sports functionalities.


Steps to execute the project in Local machine:
	
	- clone the project: git clone <url>
	- activate env: source cmsenv/bin/activate
	- run the project: python manage.py runserver

Steps to setup project from scrap:

	a. Create virtual env:
		# virtualenv -p python3 cms
	b. Activate the env:
		<path to created env>/cms/bin/activate
	c. Install requirements:
		pip3 install -r requirements.txt
	d. create migrations:
		python manage.py makemigrations
	e. Apply migrations to DB:
		python manage.py migrate
	f. load fixtures to feed sample records:
		python manage.py loaddata home/fixtures/initial.json
	g. All set, run the localhost:
		python manage.py runserver
		
Project Ingredients:

	Framework: Python3, Django 3.0, Django REST Framework 3.11
	Databse: sqlite3
	Frontend: HTML5, CSS3, jQuery
	Library: Bootstrap
	
Project Details:

Apps Used:
We have created 4 local APPS as per feasability:

	- teams
	- players
	- matches
	- points
	- home

models (Tables) created:

	- teams.Team
	- players.Player
	- matches.Match
	- points.PointTable

API URLs:

	- /teams/
	- /teams/ID:{team_id}/
	- /teams/ID:{team_id}/players/
	- /matches/                    # supporting query param for filter ?teams={comma seperated 2 team's ID like ?teams=1,2}
	- /points/
	
Template Views are defined in home APP.

All the static files including Templates, CSS, Images are defined in /static/ filder.
