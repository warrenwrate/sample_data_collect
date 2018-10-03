--drop table games

CREATE TABLE games (
    game_id text primary key,
    last_player_played text references players(player_id),
	last_move_number int CHECK (last_move_number < 17 and last_move_number > 0),
	last_col_number int CHECK (last_col_number < 5 and last_col_number > 0 ),
	result text,
	player_1 text references players(player_id),
	player_2 text references players(player_id)
);

--CREATE INDEX ON games (player_1);
--CREATE INDEX ON game (player_2);