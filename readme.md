#Token Game Data
##Overview
###Purpose:
The purpose of this project is to build a data warehouse to store the player and game related information for the popular 98point6 token (GameTokenName).
The tables and views buit should give an analyst an intuitive way to pull and anyalyse the data being stored.

###Technologies Used
1. Python 3.6
2. PostgreSQL 10.0

###Modules
The scripts to load data into the system is done with Python 3.6
Special Modules that may need installing
1. *equests* - to pull data from the REST API
2. *pyscopg2* - to connect to our PostgreSQL database

###Tables
1. Players
2. Games
3. Games Details

###Views
1. all_games_by_player - user to easly get the count of games by Nation
2. player_info - main view to get detail of how may games were played

_*Note:* Further detail on thought process can be found under the postgresqlScripts folder's readme._

##Setting up the Project
*setting up config file*
set the host, database, username, password, and csv location, log file name & location

####To set up the database, please run postgreSQL scripts in the below order
1. Players
2. Games
3. Game Details

1. column_win_prob_move_one - this is to help get the probability of a win based on the column picked on the first move.
2. all_games_by_player - used to easily get the count of the games by Nation
3. player_info - main view to get detail of how many games were played won, lossed or drawn by a player

Running the Project
To run the full project, run the "main" python file
python main.py 

Note: "A lot more detail on the classes and process can be found under the pythonProj folder's readme.


