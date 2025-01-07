--멸종위기의 대장균 찾기  https://school.programmers.co.kr/learn/courses/30/lessons/301651

with recursive GENERATIONS as (
  select 1 as GENERATION, ID as P_ID from ECOLI_DATA where PARENT_ID is null -- 재귀 초깃값
  union all
  select GENERATION + 1, ID as P_ID  -- 재귀
  from GENERATIONS G
    inner join ECOLI_DATA E on E.PARENT_ID = G.P_ID
  -- where PARENT_ID = G.P_ID -- 재귀 정지 조건
)

-- select * from GENERATIONS

select count(g.p_id) count, g.GENERATION
from (select * from GENERATIONS) G
left join ECOLI_DATA C on c.parent_id = g.p_id
where  c.id is null
group by g.GENERATION