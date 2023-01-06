from flask import Flask, Response, request
import json
from api import interface
from api import whitelist
import json


#############
# Description: This file is the main driver for the cerebro development data api.
# Run this file to start a flask API on your local machine that enables the front-end
# to get information to display about commits.
#
# NOTE: Running this file locally is not intended to be a production ready API.. use a
# dedicated WSGI server for that on a cloud platform instead.
#


##########################
# Server setup
#
app = Flask(__name__)


##########################
# Colleges methods
#

# returns all valid college IDs in the database
@app.route("/college_ids", methods = ["GET", "POST"])
def college_ids() -> json:
    result = interface.get_college_ids()
    return Response(json.dumps(result), status=200, mimetype='application/json')


# returns all information for a specific college given its id
@app.route('/college', methods = ["GET", "POST"])
def college() -> json:
    # get the user input
    college_id = request.args.get("id", None) or request.form.get("id", None)
    if college_id == None:
        # load json data if exists
        user_data = request.get_json()
        college_id = user_data.get("id", None)
    
    # ensure user provided a college id and a year
    if college_id == None:
        return Response(json.dumps("Bad request. You must provide a valid college ID"), status=400, mimetype='application/json')
    
    # cast to int types
    try:
        college_id = int(college_id)
    except BaseException:
        return Response(json.dumps("Bad request. College ID must be a valid integer."), status=400, mimetype='application/json')
    
    # validate the college id
    if college_id not in whitelist.COLLEGE_IDS:
        return Response(json.dumps("Bad request. Invalid college ID."), status=400, mimetype='application/json')
    
    result = interface.get_college(str(college_id))
    return Response(json.dumps(result), status=200, mimetype='application/json')


# returns all information for all colleges in the database
@app.route('/colleges', methods = ["GET", "POST"])
def colleges() -> json:
    result = interface.get_colleges()
    return Response(json.dumps(result), status=200, mimetype='application/json')


##########################
# Highschools methods
#


# returns all valid highschool IDs from the database
@app.route('/highschool_ids', methods = ["GET", "POST"])
def highschool_ids() -> json:
    result = interface.get_highschool_ids()
    return Response(json.dumps(result), status=200, mimetype='application/json')


# returns all information for a specific college given its id
@app.route('/highschool', methods = ["GET", "POST"])
def highschool() -> json:
    # get the user input
    highschool_id = request.args.get("id", None) or request.form.get("id", None)
    if highschool_id == None:
        # load json data if exists
        user_data = request.get_json()
        highschool_id = user_data.get("id", None)
    
    # ensure user provided a highschool id and a year
    if highschool_id == None:
        return Response(json.dumps("Bad request. You must provide a valid highschool ID"), status=400, mimetype='application/json')
    
    # cast to int types
    try:
        highschool_id = int(highschool_id)
    except BaseException:
        return Response(json.dumps("Bad request. Highschool ID must be a valid integer."), status=400, mimetype='application/json')
    
    # validate the highschool id
    if highschool_id not in whitelist.HIGHSCHOOL_IDS:
        return Response(json.dumps("Bad request. Invalid highschool ID."), status=400, mimetype='application/json')
    
    result = interface.get_highschool(str(highschool_id))
    return Response(json.dumps(result), status=200, mimetype='application/json')


# returns all information about all highschools in the database
@app.route('/highschools', methods = ["GET", "POST"])
def highschools() -> json:
    result = interface.get_highschools()
    return Response(json.dumps(result), status=200, mimetype='application/json')


##########################
# Players methods
#


# returns all information about the player with the given player id
@app.route('/player_ids', methods = ["GET", "POST"])
def player_ids() -> json:
    result = interface.get_player_ids()
    return Response(json.dumps(result), status=200, mimetype='application/json')


# returns all information about the player with the given player id
@app.route('/player', methods = ["GET", "POST"])
def player() -> json:
    # get the user input
    player_id = request.args.get("id", None) or request.form.get("id", None)
    if player_id == None:
        # load json data if exists
        user_data = request.get_json()
        player_id = user_data.get("id", None)
    
    # ensure user provided a Player ID and a year
    if player_id == None:
        return Response(json.dumps("Bad request. You must provide a valid Player ID"), status=400, mimetype='application/json')
    
    # cast to int types
    try:
        player_id = int(player_id)
    except BaseException:
        return Response(json.dumps("Bad request. Player ID must be a valid integer."), status=400, mimetype='application/json')
    
    # validate the Player ID
    if player_id not in whitelist.PLAYER_IDS:
        return Response(json.dumps("Bad request. Invalid Player ID."), status=400, mimetype='application/json')
    
    result = interface.get_player(player_id)
    return Response(json.dumps(result), status=200, mimetype='application/json')


# returns all information about all players in the database
@app.route('/players', methods = ["GET", "POST"])
def players() -> json:
    result = interface.get_players()
    return Response(json.dumps(result), status=200, mimetype='application/json')


##########################
# Commits methods
#


# returns all information about all commits for the given college ID and year
@app.route('/player_commits', methods = ["GET", "POST"])
def player_commits() -> json:
    # get the user input
    college_id = request.args.get("id", None) or request.form.get("id", None)
    year = request.args.get("year", None) or request.form.get("year", None)
    if college_id == None or year == None:
        # load json data if exists
        user_data = request.get_json()
        college_id = user_data.get("id", None)
        year = user_data.get("year", None)
    
    # ensure user provided a college id and a year
    if college_id == None or year == None:
        return Response(json.dumps("Bad request. You must provide a valid college ID and commit year."), status=400, mimetype='application/json')
    
    # cast to int types
    try:
        college_id = int(college_id)
    except BaseException:
        return Response(json.dumps("Bad request. College ID must be a valid integer."), status=400, mimetype='application/json')
    try:
        year = int(year)
    except BaseException:
        return Response(json.dumps("Bad request. Year must be a valid integer."), status=400, mimetype='application/json')
    
    # validate the college id
    if college_id not in whitelist.COLLEGE_IDS:
        return Response(json.dumps("Bad request. Invalid college ID."), status=400, mimetype='application/json')
    
    # validate the year
    if year < whitelist.COMMIT_YEARS_MIN or year > whitelist.COMMIT_YEARS_MAX:
        return Response(json.dumps("Bad request. Year provided is outside the acceptable range."), status=400, mimetype='application/json')
    
    # reasonable assurance we can pass this input to the database
    result = interface.get_commits_per_school_year(college_id, year)
    return Response(json.dumps(result), status=200, mimetype='application/json')


# returns all information about all commits in the entire database 
@app.route("/commits", methods = ["GET", "POST"])
def commits() -> json:
    result = interface.get_all_commits()
    return Response(json.dumps(result), status=200, mimetype='application/json')


# returns all valid years for commits for the given college id
@app.route("/commit_years", methods = ["GET", "POST"])
def commit_years() -> json:
    # get the user input
    college_id = request.args.get("id", None) or request.form.get("id", None)
    if college_id == None:
        # load json data if exists
        user_data = request.get_json()
        college_id = user_data.get("id", None)
    
    # ensure user provided a college id and a year
    if college_id == None:
        return Response(json.dumps("Bad request. You must provide a valid college ID"), status=400, mimetype='application/json')
    
    # cast to int types
    try:
        college_id = int(college_id)
    except BaseException:
        return Response(json.dumps("Bad request. College ID must be a valid integer."), status=400, mimetype='application/json')
    
    # validate the college id
    if college_id not in whitelist.COLLEGE_IDS:
        return Response(json.dumps("Bad request. Invalid college ID."), status=400, mimetype='application/json')
    
    result = interface.get_valid_college_commit_years(str(college_id))
    return Response(json.dumps(result), status=200, mimetype='application/json')


#########################
# Launch the server
#

def parse_config() -> json:
    with open("config.json", "r") as config:
        config = json.load(config)
    return config

if __name__ == "__main__":
    config = parse_config()
    ip = config.get("SERVER_IP", "0.0.0.0") # defaults to allow any ip to connect on your local network
    port = config.get("SERVER_PORT", 1130)
    
    app.run(ip, port)