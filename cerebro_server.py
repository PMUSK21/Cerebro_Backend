from flask import Flask, Response, request
import json
from api import config_parser
from api import interface
from api import input_validation
import json


#############
# Description: This file is the main driver for the cerebro development data api.
# Run this file to start a flask API on your local machine that enables the front-end
# to get information to display about commits.
#
# NOTE: Running this API locally is not intended to be a production ready API.. use a
# dedicated WSGI server for that on a cloud platform instead.
#


##
# Setup
#
app = Flask(__name__)
config = config_parser.parse_config()
IP = config.get("SERVER_IP", "0.0.0.0") # defaults to allow any ip to connect on your local network
PORT = config.get("SERVER_PORT", 1130) # defaults to port 1130
PRODUCTION_MODE = config.get("PRODUCTION_MODE", False) # default to false


# decorator for disabling endpoints when in production mode
def production_toggle(func):
    def wrap():
        if PRODUCTION_MODE == False:
            return func()
        else:
            return Response(json.dumps("Endpoint disabled in production mode."), status=400, mimetype='application/json')
    wrap.__name__ = func.__name__
    return wrap


##########################
# Colleges methods
#

# returns all valid college IDs in the database
@app.route("/college_ids", methods = ["GET", "POST"])
@production_toggle
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
    
    # validate the college id
    error = input_validation.validate_college_id(college_id)
    if error is not None:
        return error
    
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
@production_toggle
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
    
    # validate the highschool id
    error = input_validation.validate_highschool_id(highschool_id)
    if error is not None:
        return error
    
    result = interface.get_highschool(str(highschool_id))
    return Response(json.dumps(result), status=200, mimetype='application/json')


# returns all information about all highschools in the database
@app.route('/highschools', methods = ["GET", "POST"])
@production_toggle
def highschools() -> json:
    result = interface.get_highschools()
    return Response(json.dumps(result), status=200, mimetype='application/json')


##########################
# Players methods
#


# returns all information about the player with the given player id
@app.route('/player_ids', methods = ["GET", "POST"])
@production_toggle
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
    
    # validate the player id
    error = input_validation.validate_player_id(player_id)
    if error is not None:
        return error
    
    result = interface.get_player(player_id)
    return Response(json.dumps(result), status=200, mimetype='application/json')


# returns all information about all players in the database
@app.route('/players', methods = ["GET", "POST"])
@production_toggle
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
    
    # validate the user college id
    error = input_validation.validate_college_id(college_id)
    if error is not None:
        return error
    
    # validate the year
    error = input_validation.validate_commit_year(year)
    if error is not None:
        return error
    
    # reasonable assurance we can pass this input to the database
    result = interface.get_commits_per_school_year(college_id, year)
    return Response(json.dumps(result), status=200, mimetype='application/json')


# returns all information about all commits in the entire database
@app.route("/commits", methods = ["GET", "POST"])
@production_toggle
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
    
    # validate the user input
    error = input_validation.validate_college_id(college_id)
    if error is not None:
        return error
    
    result = interface.get_valid_college_commit_years(str(college_id))
    return Response(json.dumps(result), status=200, mimetype='application/json')


#########################
# Launch the server
#

if __name__ == "__main__":
    app.run(IP, PORT)