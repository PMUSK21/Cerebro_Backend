import json
import os
import database as db
    
def _nullify(val):
    if val == "N/A":
        return None
    if val == '':
        return None
    return val
    
def _handle_commits_json(data:dict, all_data:dict) -> None:
    return # safeguard
    # parse the college info
    db.create.add_college(data['school'], data['conference'])
    db.commit()
    college_db_data = db.query.get_colleges(data['school'], data['conference'])
    
    for year in data['commits']:
        commit_actions = data['commits'][year]['category']
        for commit_action in commit_actions:
            players = commit_actions[commit_action]
            for player in players:
                hs_name = player['highschool_name']
                hs_location_split = player['highschool_location'].split(", ")
                if len(hs_location_split) != 2:
                    hs_state = None
                    hs_city = None
                else:
                    hs_city, hs_state = hs_location_split
                db.create.add_highschool(hs_name, hs_city, hs_state)
                db.commit()
                try:
                    highschool_data = db.query.get_highschool_by_attributes(hs_name, hs_city, hs_state)
                except BaseException:
                    highschool_data = {'id':None}
                db.create.add_player(player['id'], player['name'], player['url'], player['profile_image'])
                college_id = _nullify(college_db_data[0].get('id', None))
                highschool_id = _nullify(highschool_data.get('id', None))
                position = _nullify(player['position'])
                national_rank = _nullify(player['national_rank'])
                state_rank = _nullify(player['state_rank'])
                positional_rank = _nullify(player['positional_rank'])
                rating = _nullify(player['rating'])
                height = _nullify(player['height'])
                weight_lbs = _nullify(player['weight'])
                status = _nullify(player['status'])
                commit_date = _nullify(player['commit_date'])
                db.create.add_commit(player['id'], year, college_id, highschool_id, position, national_rank, state_rank, positional_rank, rating, \
                    height, weight_lbs, status, commit_action, commit_date)
                db.commit()
            
    return

def load_commits() -> None:
    return # safeguard
    path = "resources/Commits/Football/data/"
    files = os.listdir(path)
    
    db.create.create_tables()
    db.commit()
    
    all_data = {}
    for file in files:
        print("Loading {}".format(file))
        with open(path+file, 'r') as infile:
            data = json.loads(infile.read())
        _handle_commits_json(data, all_data)    

def __append_columns_hs() -> None:
    return # safeguard
    command = """
    ALTER TABLE highschools
    ADD COLUMN full_address TEXT
    """
    db.CUR.execute(command)
    command = """
    ALTER TABLE highschools
    ADD COLUMN address_types TEXT
    """
    db.CUR.execute(command)
    command = """
    ALTER TABLE colleges
    ADD COLUMN full_address TEXT
    """
    db.CUR.execute(command)
    command = """
    ALTER TABLE colleges
    ADD COLUMN address_types TEXT
    """
    db.CUR.execute(command)
    #db.con.commit()

def __append_fullname_colleges() -> None:
    return # safeguard
    command = """
    ALTER TABLE colleges
    ADD COLUMN full_name TEXT
    """
    db.CUR.execute(command)
    db.con.commit()

if __name__=="__main__":
    #load_commits()
    #__append_columns()
    #__append_columns_college()
    pass