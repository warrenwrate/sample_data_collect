
-- drop view column_win_prob_move_one
create view column_win_prob_move_one as

select distinct gt.column_number,
ROUND(
(cast(count(*) over(partition by gt.column_number) as decimal )/ cast( count(*) over() as decimal) * 100)
,4) as percentile,
count(*) over() as total
from game_details gt
join games g on gt.game_id = g.game_id
where g.result = 'win' and gt.move_number = 1
order by percentile desc
;

select column_number,(percent_rank() OVER win)::numeric(10, 2) as percentile_rank
FROM column_win_prob_move_one 
WINDOW win AS (ORDER BY column_number);
