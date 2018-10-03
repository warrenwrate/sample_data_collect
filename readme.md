# Token Game Data
## Overview
### Purpose:
The purpose of this project is to build a data warehouse to store the player and game related information for the popular 98point6 token game (Drop Token).
The tables and views built should give an analyst an intuitive way to pull and anyalyse the data being stored.

### Technologies Used
1. Python 3.6
2. PostgreSQL 10.0
### Modules
The scripts to load data into the system is done with Python 3.6
Special Modules that may need installing...
1. **requests** - to pull data from the REST API
2. **pyscopg2** - to connect to our PostgreSQL database

### Tables
1. **players** - this is the data gathered by the REST API given.
2. **games** - the games data was produced, to evaluate each game by (win,loss, or draw), players, last move and player that conducted the last move.
3. **game_details** - is the complete gaming details from the csv.

### Views
1. **all_games_by_player** - this is a union created from the games table using player1 and player2 to get all games played by each player.
2. **player_info** - the player info table is an add-on view on top of **all_games_by_player view** to count the total games, wins, losses, and draws by player.
3. **column_win_prob_move_one** - this view is a join between the **games** and **game_details** table, which partitions the count of column numbers and total overall count.
   ..* Then I divide the totals to give me a perecentage of how each column may have given a slight advantage.


## Setting up the Project
The first item is to set up the [config file](https://github.com/warrenwrate/token_project/blob/master/pythonproj/configdata.cfg).
This is a way to set the variables once, and not have the need to do it again.
Set the **host**, **database**, **username**, **password**, and **csv location**, **log file name & location**

##### To set up the database, please run postgreSQL scripts in the below order
1. **players_table.sql** - creates the **players** table
2. **games_table.sql** - creates the **games** table
3. **gamesdetail_table.sql** - creates the **game_details** table
4. **percentile_rank.sql** - this creates the **column_win_prob_move_one** view and has the query which is used for the first question.
5. **playerviews.sql** - this creates the **all_games_by_player** view, has a query for question two, then creates the **player_info** view to assist with the final question.


## Running the Project
To run the full project, run the "main" python file
```python
python main.py
```
#### Detail
1. **main.py** - ties all of the functionality into one last module.
2. **connections.py** - used to gather the connections, and then is inherited by other classes for logging and holding database connections.
3. **loadplayer.py** - this is used to load the player data. 
4. **loadgame.py** - runs a process to get the data that is used for the **games** table.
5. **loadgamedetails.py** - pulls the detailed game data from the csv to the database.
6. **player.py** - this is a class that I created that helped me manage the player data.



## Questions and Querable Answers

1. Out of all the games, what is the percentile rank of each column used as the
   first move in a game? That is, when the first player is choosing a column
   for their first move, which column most frequently leads to that player
   winning the game?

```sql
select column_number,
(percent_rank() OVER win)::numeric(10, 2) as percentile_rank
FROM column_win_prob_move_one 
WINDOW win AS (ORDER BY column_number);
```
2. How many games has each nationality participated in?
```sql
select p.nat, count(*) TotalCount
from players as p
join all_games_by_player as agp on p.playerid = agp.player
group by p.nat
order by count(*) desc
```

3. Marketing wants to send emails to players that have only played a single
   game. The email will be customized based on whether or not the player won,
   lost, or drew the game. Which players should receive an email, and with what
   customization?
```sql
select p.email,
case when win_count = 1 then concat('hello ', p.firstname, ' ', p.lastname ,
	'\nI get it...retiring as CHAMP!!\nTry playing again to add to your legacy!')
	 when loss_count = 1 then concat('hello ', p.firstname, ' ', p.lastname ,
	'\nLosing is no fun, but you need to try again.\nYou can do it! We BELIEVE!!!')
	 when draw_count = 1 then concat('hello ', p.firstname, ' ', p.lastname ,
	'\nLook out partner now... DRAW.\nBut that is not all you should do.  Please play again.') else 'uh oh no value' end custom_message
from player_info p_info
join players p on p_info.player = p.playerid
where total_count = 1
```
