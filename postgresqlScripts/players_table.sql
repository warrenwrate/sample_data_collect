
--drop table players

CREATE TABLE players (
    player_id text PRIMARY key,
    firstname text,
	lastname text,
	title text,
	gender text,
	street text,
	city text,
	state text,
	postcode text,
	email text,
	dob date,
	phone text,
	cell text,
	nat text,
	registered date,
	largeimage text,
	mediumimage text,
	thumbnail text,
	id_name text,
	id_value text
);