
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
select p.nat, count(*) TotalCount
from players as p
join all_games_by_player as agp on p.playerid = agp.player
group by p.nat
order by count(*) desc



-- drop view player_info
create view player_info as

select p.player, 
coalesce(draw_count, 0) draw_count,
coalesce(win_count, 0) win_count,
coalesce(loss_count, 0) loss_count
, count(*) total_count
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


-- custom statments for players only game was a win, loss, or draw
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
