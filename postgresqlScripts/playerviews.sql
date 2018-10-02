
--drop view all_games_by_player

create view all_games_by_player as

select game_id, last_player_played, last_move_number,
case when result = 'win' and last_player_played <> player_1 then'loss'
	 when result = 'win' and last_player_played = player_1 then 'win'
	 else 'draw' end result
, player_1 player
from games

union all

select game_id, last_player_played, last_move_number, 
case when result = 'win' and last_player_played <> player_2 then'loss'
	 when result = 'win' and last_player_played = player_2 then 'win'
	 else 'draw' end result
, player_2
from games

-- above looks good
-- most games by nation
select p.nat, count(*)
from players as p
join all_games_by_player as agp on p.playerid = agp.player
group by p.nat
order by count(*) desc


-- Partition Example
select distinct player, result, 
count(*) over(partition by player, result) as by_result,
count(*) over(partition by player) as total
from all_games_by_player
order by player, result
limit 10

-- drop view player_info
create view player_info as

select p.player, 
coalesce(draw_count, 0) draw_count,
coalesce(win_count, 0) win_count,
coalesce(loss_count, 0) loss_count
, count(*) TotalCount
from all_games_by_player p
left join 
	(select player, count(*) draw_count
	from all_games_by_player
	where result = 'draw' --and player = 1 
	group by player) draw on p.player = draw.player
left join 
	(select player, count(*) win_count
	from all_games_by_player
	where result = 'win' --and player = 1 
	group by player) win on p.player = win.player
left join 
	(select player, count(*) loss_count
	from all_games_by_player
	where result = 'loss' --and player = 1 
	group by player) loss on p.player = loss.player
group by p.player, draw_count, win_count, loss_count


select * from player_info 
where totalcount = 1
order by player
limit 10

select *
from all_games_by_player p
where p.player = 88



select *
from all_games_by_player
where result = 'loss' and player = 1

select *
from all_games_by_player
where result = 'win' and player = 1

