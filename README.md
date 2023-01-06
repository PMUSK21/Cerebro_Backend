# CEREBRO 113 Server API

## Purpose

This repository is dedicated to the backend development of the brains behind **Cerebro 113**; practically speaking, this includes database management and a secure REST API access to it.

## Installation

You are required to have Python3. I recommend getting the latest release from the following link if you don't already have Python3:

[Download Python Here](https://www.python.org/downloads/)

At the root level of this project, run this command:
```
pip install -e .
```

## Configuration

The API can be configured through the use of the *config.json* file located at the root directory of this repo. The config file specifies three parameters you may change:

- SERVER_IP
- SERVER_PORT
- PRODUCTION_MODE

By default, the server IP is set to **0.0.0.0**, which runs the server on ip address *127.0.0.1* but allows anyone on your local network to connect to the server as long as firewall permissions are set up correctly. The port is set to **1130**. You can change these settings by modifying the *config.json* file and then restarting the API.

*PRODUCTION_MODE* is defaulted to *false*. When *PRODUCTION_MODE* is enabled, the endpoints that are noted below will not be enabled as to avoid anyone from using them and hogging your servers resources.

*PRODUCTION_MODE* is designed to allow development to be effecient by exposing database queries that help the developers of the front end see the data available in the database. It is important to not host this API in a publically available manner when *PRODUCTION_MODE* is set to *False* -- this will expose all of your data to anyone, and also enable someone to hog all the server system resources.

In short: *PRODUCTION_MODE* set to *False* is perfectly acceptable to be used at any point in time, except for when you want to deploy Cerebro 113 to the world.

## Running API

To start the development API server on windows, use the following command prompt command at the root level of this directory:
```
python .\cerebro_server.py
```

To run on linux, enter this command instead:
```
python cerebro_server.py
```

**NOTE: You may have to specify *python3* in the commands above depending on how it was installed on your machine**

# Endpoints:

The following are all the available endpoints that you can access via http GET or POST requests.

*Note: For testing, you can enter any of the example commands below in your browser while the API is running to see the result of the request.*

## /college_ids

Takes no arguments and returns a list of valid college id's in the database.

Example:
```
127.0.0.1:1130/college_ids
```

*NOTE: Disabled in production mode*

## /college

Takes a named argument **id** and returns a json object with information about that college.

Example:
```
127.0.0.1:1130/college?id=123
```

## /colleges

Takes no arguments and returns a large list of all information of every college in the database.

Example:
```
127.0.0.1:1130/colleges
```

## /highschool_ids

Takes no arguments and returns a list of valid highschool ids in the database.

Example:
```
127.0.0.1:1130/highschool_ids
```

*NOTE: Disabled in production mode*

## /highschool

Takes a named argument **id** and returns a json object with information about that highschool.

Example:
```
127.0.0.1:1130/highschool?id=111
```

## /highschools

Takes no arguments and returns a large list of all information of every highschool in the database.

Example:
```
127.0.0.1:1130/highschools
```

*NOTE: Disabled in production mode*

## /player_ids

Takes no arguments and returns a list of valid player ids in the database.

Example:
```
127.0.0.1:1130/player_ids
```

*NOTE: Disabled in production mode*

## /player

Takes a named argument **id** and returns a json object with information about that player.

Example:
```
127.0.0.1:1130/player?id=139
```

## /players

Takes no arguments and returns a large list of all information of every player in the database.

Example:
```
127.0.0.1:1130/players
```

*NOTE: Disabled in production mode*

## /player_commits

Takes 2 named arguments, college **id** and commit **year**, and returns a json object with information about all the player commits for the given college for the given year.

Example:
```
127.0.0.1:1130/player_commits?id=123&year=2018
```

## /commits

Takes no arguments and returns a large list of all information of every player commit in the database.

Example:
```
127.0.0.1:1130/commits
```

*NOTE: Disabled in production mode*

## /commit_years

Takes a named argument college **id** and returns a list of all valid commit years for that college.

Example:
```
127.0.0.1:1130/commit_years?id=123
```