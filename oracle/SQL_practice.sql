--1.회원별 주문 상품 통계
--회원아이디 상품번호 상품갯수 구매금액
--(조건:주문건이 없더라도 회원출력)

select u.user_ID, og.good_seq, og.order_amount, og.order_price
from users u, orders_goods og, orders o
where u.user_seq=o.user_seq(+) and o.order_code = og.order_code(+)
order by user_id asc, good_seq asc;



--2.업체별 공급 상품 리스트
--업체번호 업체명 상품번호 상품명
--(조건:상품이 없더라도 업체명 출력)

select c.com_seq, c.com_name, g.good_seq, g.good_name
from company c, company_goods cg, goods g
where c.com_seq=cg.com_seq(+) and cg.good_seq=g.good_seq(+)
order by c.com_seq, g.good_seq;



--3.회원관리
--정규직/비정규직 구분하여 출력 
--조건1:정규직이면A,비정규직이면B로 출력
--조건2:급여(1일 8시간 한달:20일 기준으로 계산)
--회원번호 회원명 정규/비정규여부 월급여

select u.user_seq, u.user_name, f.asal/12 as monthsal_full, (p.tsal*8*20) as monthsal_part, 
case
  when u.user_seq in (select user_seq from fulltime where asal is not null) then 'A'
  when u.user_seq in (select user_seq from parttime where tsal is not null) then 'B'
 end
from users u, fulltime f, parttime p
where u.user_seq=f.user_seq(+) and p.user_seq(+)=u.user_seq;

(select u.user_seq, u.user_name, f.asal/12 as monthsal_full, 'A' as gubun
from users u, fulltime f
where u.user_seq=f.user_seq)
 union
(select u.user_seq, u.user_name, (p.tsal*8*20) as monthsal_part, 'B' as gubun
from users u, parttime p
where u.user_seq=p.user_seq);



--4.상품/주문관리
--주문된 상품별 판매량, 판매금액 출력
--조건:판매량이 높은 순으로 정렬
--상품번호 상품명 총판매량 총판매금액

select g.good_seq, g.good_name, sum(og.order_amount) as totamount, sum(og.order_price) as totprice
from orders_goods og, goods g
where og.good_seq=g.good_seq
group by g.good_seq, g.good_name
order by totamount desc;



--5. 사용자별 구매 통계
--회원아이디  총구매횟수   총구매금액
--조건1 : 구매금액이 높은 순 출력

select u.user_id, count(o.order_code) as cnt, sum(tot_price) as totprice
from users u, orders o
where u.user_seq=o.user_seq
group by  u.user_id
order by sum(tot_price) desc;


--6. 휴먼회원 통계
--구매실적이 전혀 없는 회원 목록 출력
--회원아이디 회원명  

select user_id,user_name
from users
where user_seq not in (select user_seq from orders);



--7. 전체 회원 목록 중 휴먼 회원이 차지하는 비율?
--조건1 : 관리자 제외
--조건2: 휴먼회원은 구매 실적이 전혀 없는 회원
-- 회원수   휴먼회원비율
--------- 
--  2/5      40%       

select (select count(user_seq)
        from users
        where user_seq not in (select user_seq from orders)) 
        || '/' 
        || (select count(1) from users where user_id <> 'admin') 
        , (select count(user_seq)
        from users
        where user_seq not in (select user_seq from orders))
        /(select count(1) from users where user_id <> 'admin') * 100
        || '%' 
from dual;

select (hcnt || '/' || allcnt) as cnt, (hcnt/allcnt*100 || '%' ) as rate
from (select count(user_seq) as hcnt
        from users
        where user_seq not in (select user_seq from orders))  h, (select count(user_seq) as allcnt from users) u;


--8. 각 회원별로 매니저-회원 관계를 출력하시오
--조건1: 관리자 제외
--조건2: 매니저번호 오름차순 회원번호 오름차순 정렬

--매니저  회원  
--lee	kim
--lee     park
--prak    hong

select (u2.user_id) as mgr, (u1.user_id) as cli
from users u1, users u2
where u1.mgr_seq=u2.user_seq
and u1.user_id <> 'admin' and u2.user_id <> 'admin'
order by mgr asc, cli asc;
  
--n00005	4	14000
--n00011	4	40000


--9. 주문/상품/업체 대시보드 현황판

-- 총주문수량 총주문금액  총회원수  총업체수 총상품수
-- 58         1025000     5         7        12

--       AMT      PRICE       UCNT       CCNT       GCNT
---------- ---------- ---------- ---------- ----------
--        48     244000          5          7         10

select (select sum(order_amount) from orders_goods) as 총주문수량
      ,(select sum(tot_price) from orders) as 총주문금액
      ,(select sum(order_price) from orders_goods) as 총주문금액2
      ,(select count(user_seq) from users) as 총회원수
      ,(select count(com_Seq) from company) as 총업체수
      ,(select count(good_Seq) from goods) as 총상품수
from dual;

select o.order_code , o.order_price , a.tot_price , a.order_code
from orders_goods o, orders a
where  o.order_code= a.order_code
order by o.order_code, a.order_code;


--10.월별 판매 실적....
--  1월   2월   3월   4월  
-- 20000  12000  50000

select sum(decode(to_char(order_date,'mm'),01,tot_price)) as JAN
      ,sum(decode(to_char(order_Date,'mm'),02,tot_price)) as FEB
      ,sum(decode(to_char(order_Date,'mm'),03,tot_price)) as MAR
      ,sum(decode(to_char(order_Date,'mm'),04,tot_price)) as APRL
      ,sum(decode(to_char(order_Date,'mm'),05,tot_price)) as MAY
      ,sum(decode(to_char(order_Date,'mm'),06,tot_price)) as JUN
      ,sum(decode(to_char(order_Date,'mm'),07,tot_price)) as JUL
      ,sum(decode(to_char(order_Date,'mm'),08,tot_price)) as AUG
      ,sum(decode(to_char(order_Date,'mm'),09,tot_price)) as SEP
      ,sum(decode(to_char(order_Date,'mm'),10,tot_price)) as OCT
      ,sum(decode(to_char(order_Date,'mm'),11,tot_price)) as NOV
      ,sum(decode(to_char(order_Date,'mm'),12,tot_price)) as DEC
from orders;


--11 회원 포인트 등급
select grade
from 
(
        select gpoint_start, decode(gpoint_end ,null, 999999, gpoint_end-1) as gpoint_end,  grade
        from 
        (select g.gpoint_start , g.grade
                , (select gpoint_start from grade_info where seq = g.seq+1) as gpoint_end
        from grade_info g
        ) 
) t
where  (select sum(point) from point_info where user_num=1)  between gpoint_start and gpoint_end;