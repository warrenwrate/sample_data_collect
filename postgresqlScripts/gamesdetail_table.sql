--drop table game_details

CREATE TABLE game_details (
	game_detais_id serial primary key,
    game_id text references games(game_id),
    player_id text references players(player_id)  ,
	move_number int CHECK (move_number < 17 and move_number > 0),
	column_number int CHECK (column_number < 5 and column_number > 0 ),
	result text
);

-- select * from game_details