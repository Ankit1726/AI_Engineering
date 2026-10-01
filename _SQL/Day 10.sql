-- SQL  Series Day 10 (View In SQL)
use banK_server;
select * from account_record;

create view v1 as select accound_id,name from account_record;
select * from v1 where name = "Ian Malcolm";
drop view v1;

use restuarent;
select * from customer;
select * from orders;

create view v2 as select c.customer_id ,c.name,o.order_id
from customer c
inner join orders o
on c.customer_id = o.customer_id;

select * from v2 where name = "Diana Prince";
select * from v2;