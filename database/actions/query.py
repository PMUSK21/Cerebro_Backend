def get_college_ids(cursor) -> list:
    c = cursor.execute("SELECT id FROM colleges")
    return [dict(row)['id'] for row in c.fetchall()]

def get_colleges(cursor, id:str=None, name:str=None, conference:str=None) -> list:
  query = "SELECT * FROM colleges"
  match_criteria = []
  
  if id:
    match_criteria.append("id = \"{}\"".format(str(id)))
  if name:
    match_criteria.append("name = \"{}\"".format(name))
  if conference:
    match_criteria.append("conference = \"{}\"".format(conference))
  
  if len(match_criteria) != 0:
    query += " WHERE "
    query += " AND ".join(match_criteria)
  
  c = cursor.execute(query)
  return [dict(row) for row in c.fetchall()]

def get_highschool_ids(cursor) -> list:
    c = cursor.execute("SELECT id FROM highschools")
    return [dict(row)['id'] for row in c.fetchall()]

def get_highschool_by_attributes(cursor, name:str, city:str, state:str) -> dict:
  c = cursor.execute("SELECT * from highschools WHERE (name=? AND city=? AND state=?)", (name, city, state))
  return dict(c.fetchone())

def get_highschool(cursor, id:str) -> dict:
  c = cursor.execute("SELECT * from highschools WHERE (id=?)", [(id)])
  return dict(c.fetchone())

def get_all_highschools(cursor) -> list:
  c = cursor.execute("SELECT * FROM highschools")
  return [dict(row) for row in c.fetchall()] 

def get_player_ids(cursor) -> list:
  c = cursor.execute("SELECT id FROM players")
  return [dict(row)['id'] for row in c.fetchall()]

def get_player(cursor, id:str) -> dict:
  query = "SELECT * FROM players WHERE (id = ?)"
  c = cursor.execute(query, [(id)])
  return dict(c.fetchone())

def get_players(cursor) -> list:
  c = cursor.execute("SELECT * FROM players")
  return [dict(row) for row in c.fetchall()]  

def get_players_for_school(cursor, school_id:str, year:str) -> list:
  query = """
  SELECT players.id as player_id, players.name as player_name, height AS player_height, weight_lbs AS player_weight, profile_url AS player_profile_url, profile_image AS player_image,
    national_rank AS commit_national_rank, state_rank AS commit_state_rank, positional_rank AS commit_positional_rank, rating AS commit_rating, position AS commit_position, year AS commit_year, status AS commit_status, commit_action, commit_date,
    colleges.name AS college_name,
    highschools.city AS hs_city, highschools.state AS hs_stae, highschools.latitude AS hs_latitude, highschools.longitude AS hs_longitude, highschools.name AS hs_name
  FROM colleges
  INNER JOIN player_commits ON player_commits.college_id = colleges.id
  INNER JOIN players ON player_commits.player_id = players.id
  INNER JOIN highschools ON highschools.id = player_commits.highschool_id
  WHERE (colleges.id = ? AND player_commits.year = ?)"""
  c = cursor.execute(query, (str(school_id), str(year)))
  return [dict(row) for row in c.fetchall()]

def get_available_colleges(cursor) -> list:
  query = """SELECT name, full_name, id FROM colleges"""
  c = cursor.execute(query)
  return [dict(row) for row in c.fetchall()]
  
def get_all_commits(cursor) -> list:
  query = """SELECT * FROM player_commits"""
  c = cursor.execute(query)
  return [dict(row) for row in c.fetchall()]

def get_all_unique_commit_years(cursor) -> list:
  query = """SELECT DISTINCT year FROM player_commits"""
  c = cursor.execute(query)
  return [dict(row)['year'] for row in c.fetchall()]

def get_valid_college_commit_years(cursor, college_id:str) -> list:
  query = """SELECT DISTINCT year FROM player_commits WHERE college_id = ?"""
  c = cursor.execute(query, [(college_id)])
  return [dict(row)['year'] for row in c.fetchall()]