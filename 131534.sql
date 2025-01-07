-- 상품을 구매한 회원 비율 구하기

SELECT B.YEAR, TO_NUMBER(B.MONTH),count(B.PUCHASED_USERS) ,
        ROUND(count(B.PUCHASED_USERS) / (
            select count(*)
                from USER_INFO
                where TO_CHAR(joined,'YYYY') = '2021') 
        ,1) as PUCHASED_RATIO
FROM (SELECT TO_CHAR(B.Sales_date,'YYYY') AS YEAR, TO_CHAR(B.Sales_date,'MM') AS MONTH,
        count(B.USER_ID) as PUCHASED_USERS
    from USER_INFO A
        inner join ONLINE_SALE B
        on A.USER_ID = B.USER_ID
    where TO_CHAR(A.joined,'YYYY') = '2021'
        group by TO_CHAR(B.Sales_date,'YYYY'), TO_CHAR(B.Sales_date,'MM'), B.USER_ID) B
    GROUP BY B.YEAR, B.MONTH
    ORDER BY B.YEAR, B.MONTH