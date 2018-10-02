--drop table games

CREATE TABLE games (
    game_id text primary key,
    last_player_played int references players(playerid),
	last_move_number int CHECK (last_move_number < 17 and last_move_number > 0),
	last_col_number int CHECK (last_col_number < 5 and last_col_number > 0 ),
	result text,
	player_1 int references players(playerid),
	player_2 int references players(playerid)
);

--CREATE INDEX ON games (player_1);
--CREATE INDEX ON game (player_2);