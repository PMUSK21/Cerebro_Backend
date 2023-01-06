from api import interface

#############
# Description: To avoid SQL injections, unintended access, and
# unnecessary performance degredation to this API, checking user
# provided values against a whitelist for that parameter is
# important. This file specifies some whitelisted values that 
# correspond to user input from various endpoints.
#

PLAYER_IDS = set(interface.get_player_ids())
COLLEGE_IDS = set(interface.get_college_ids())
HIGHSCHOOL_IDS = set(interface.get_highschool_ids())
COMMIT_YEARS_MIN = min(interface.get_all_unique_commit_years())
COMMIT_YEARS_MAX = max(interface.get_all_unique_commit_years())
