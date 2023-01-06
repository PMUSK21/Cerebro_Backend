import json

##############
# Description: Parses the json config file to set up the api
#

def parse_config() -> json:
    with open("config.json", "r") as config:
        config = json.load(config)
    return config