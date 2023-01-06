from database import database as db
import sqlite3


#############
# Description: This class is a collection of wrappers for interfacing with the database.
# Each wrapper gets a unique connection to the database for the thread that is running
# the command. This ensure SQLite is happy with the threaded nature of flask API handlers.
#

def get_db_connection() -> sqlite3.Connection:
    conn = sqlite3.connect("database/commits.db")
    conn.row_factory = sqlite3.Row
    return conn

def get_college_ids() -> list:
    conn = get_db_connection()
    result = db.query.get_college_ids(conn.cursor())
    conn.close()
    return sorted(result)

def get_college(id:str) -> dict:
    conn = get_db_connection()
    result = db.query.get_colleges(conn.cursor(), id)
    conn.close()
    return result

def get_colleges() -> list:
    conn = get_db_connection()
    result = db.query.get_colleges(conn.cursor())
    conn.close()
    return result

def get_player_ids() -> list:
    conn = get_db_connection()
    result = db.query.get_player_ids(conn.cursor())
    conn.close()
    return sorted(result)

def get_player(id:str) -> dict:
    conn = get_db_connection()
    result = db.query.get_player(conn.cursor(), id)
    conn.close()
    return result

def get_players() -> list:
    conn = get_db_connection()
    result = db.query.get_players(conn.cursor())
    conn.close()
    return result

def get_highschool_ids() -> list:
    conn = get_db_connection()
    result = db.query.get_highschool_ids(conn.cursor())
    conn.close()
    return sorted(result)

def get_highschool(id:str) -> dict:
    conn = get_db_connection()
    result = db.query.get_highschool(conn.cursor(), id)
    conn.close()
    return result

def get_highschools() -> list:
    conn = get_db_connection()
    result = db.query.get_all_highschools(conn.cursor())
    conn.close()
    return result

def get_commits_per_school_year(school_id:str, year:int) -> list:
    conn = get_db_connection()
    result = db.query.get_players_for_school(conn.cursor(), school_id, year)
    conn.close()
    return result

def get_all_unique_commit_years() -> list:
    conn = get_db_connection()
    result = db.query.get_all_unique_commit_years(conn.cursor())
    conn.close()
    return sorted(result)

def get_valid_college_commit_years(college_id:str) -> list:
    conn = get_db_connection()
    result = db.query.get_valid_college_commit_years(conn.cursor(), college_id)
    conn.close()
    return sorted(result)

def get_all_commits() -> list:
    conn = get_db_connection()
    result = db.query.get_all_commits(conn.cursor())
    conn.close()
    return result