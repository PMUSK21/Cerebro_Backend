def create_tables(cursor) -> None:
    cursor.execute("CREATE TABLE IF NOT EXISTS colleges(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, full_name TEXT, conference TEXT NOT NULL, city TEXT, state TEXT, full_address TEXT, latitude REAL, longitude REAL, UNIQUE(name, conference))")
    cursor.execute("CREATE TABLE IF NOT EXISTS highschools(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, city TEXT NOT NULL, state TEXT NOT NULL, full_address TEXT, latitude REAL, longitude REAL, UNIQUE (name, city, state))")
    cursor.execute("CREATE TABLE IF NOT EXISTS players(id INTEGER PRIMARY KEY, name TEXT, profile_url TEXT, profile_image TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS player_commits(player_id INTEGER, year INTEGER, college_id INTEGER, highschool_id INTEGER,\
        position TEXT, national_rank INTEGER, state_rank INTEGER, positional_rank INTEGER, rating REAL, height TEXT, weight_lbs INTEGER,\
        status TEXT, commit_action TEXT, commit_date TEXT, \
        FOREIGN KEY (player_id) REFERENCES players (id), \
        FOREIGN KEY (college_id) REFERENCES colleges (id), \
        FOREIGN KEY (highschool_id) REFERENCES highschools (id),\
        PRIMARY KEY (player_id, year, college_id, status))")
    
def add_college(cursor, name:str, conference:str) -> None:
    cursor.execute("INSERT OR IGNORE INTO colleges(name, conference) VALUES (?,?)", (name,conference))

def add_highschool(cursor, name:str, city:str, state:str) -> None:
    cursor.execute("INSERT OR IGNORE INTO highschools(name, city, state) VALUES (?,?,?)", (name, city, state))

def add_player(cursor, id:int, name:str, profile_url:str, profile_image:str) -> None:
    cursor.execute("INSERT OR IGNORE INTO players(id, name, profile_url, profile_image) VALUES (?,?,?,?)", (id, name, profile_url, profile_image))

def add_commit(cursor, player_id:int, year:int, college_id:int, highschool_id:int, position:str, national_rank:int, state_rank:int, positional_rank:int,\
    rating:float, height:str, weight_lbs:int, status:str, commit_action:str, commit_date:str) -> None:
    cursor.execute("INSERT OR IGNORE INTO player_commits(player_id, year, college_id, highschool_id, position, national_rank, state_rank, positional_rank,\
        rating, height, weight_lbs, status, commit_action, commit_date) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",\
        (player_id, year, college_id, highschool_id, position, national_rank, state_rank, positional_rank,\
        rating, height, weight_lbs, status, commit_action, commit_date))