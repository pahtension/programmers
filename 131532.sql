--년, 월, 성별 별 상품 구매 회원 수 구하기

select year, TO_NUMBER(month), gender, count(user_id) users
from (SELECT TO_CHAR(SALES_DATE,'YYYY') year, TO_CHAR(SALES_DATE,'MM') month, 
           O.user_id, U.gender
    FROM ONLINE_SALE O
    inner join USER_INFO U
        ON O.user_id = U.user_id AND U.gender is not null
    GROUP BY O.user_id, U.gender, 
             TO_CHAR(SALES_DATE,'YYYY'), TO_CHAR(SALES_DATE,'MM')
    ) 
group by year, month, gender
order by year, month, gender