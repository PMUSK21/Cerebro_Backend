from typing import Any
from flask import Response
from api import whitelist
import json

##############
# Description: Input validation is an important step to pass through when working
# with API's. This file provides some methods to validate whether the values 
# users pass into the API are valid and safe before doing anything with these values
# in conjunction with the database.
# 


# Validates whether a value is a valid college id.
# Returns an error response if it is invalid, else it returns
# a None object to signify no error.
#
def validate_college_id(college_id:Any) -> Any:
    # ensure user provided a college id
    if college_id == None:
        return Response(json.dumps("Bad request. You must provide a valid college ID"), status=400, mimetype='application/json')
    
    # cast to int type
    try:
        college_id = int(college_id)
    except BaseException:
        return Response(json.dumps("Bad request. College ID must be a valid integer."), status=400, mimetype='application/json')
    
    # validate the college id
    if college_id not in whitelist.COLLEGE_IDS:
        return Response(json.dumps("Bad request. Invalid college ID."), status=400, mimetype='application/json')

    # this is a valid college id, return no error
    return None


# Validates whether a value is a valid commit year.
# Returns an error response if it is invalid, else it returns
# a None object to signify no error.
#
def validate_commit_year(year:Any) -> Any:
    # ensure the user provided a year
    if year == None:
        return Response(json.dumps("Bad request. You must provide a valid commit year."), status=400, mimetype='application/json')
    
    # cast to int type
    try:
        year = int(year)
    except BaseException:
        return Response(json.dumps("Bad request. Year must be a valid integer."), status=400, mimetype='application/json')
    
    # validate year is in correct range
    if year < whitelist.COMMIT_YEARS_MIN or year > whitelist.COMMIT_YEARS_MAX:
        return Response(json.dumps("Bad request. Year provided is outside the acceptable range."), status=400, mimetype='application/json')
    
    # this is a valid commit year
    return None


# Validates whether a value is a valid player id.
# Returns an error response if it is invalid, else it returns
# a None object to signify no error.
#
def validate_player_id(player_id:Any) -> Any:
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
    
    # this is a valid player id
    return None


# Validates whether a value is a valid highschool id.
# Returns an error response if it is invalid, else it returns
# a None object to signify no error.
#
def validate_highschool_id(highschool_id:Any) -> Any:
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
    
    # this is a valid highschool id
    return None