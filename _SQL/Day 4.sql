-- SQL  Series Day 4 

use instagram;
select * from user;

-- Apply Aggregate Functions 
select age,count(age) from user where age = 21;
select sum(follwers) from user;

select max(following) from user;
select min(follwers) from user;
select avg(follwers) from user;

-- Groupby Clause 
select age,count(id) from user group by age;

select age,max(follwers) from user group by age 
having max(follwers) > 200 order by age asc;

-- Table Queries 
select * from insta_user;
set sql_safe_updates = 0;
update user set follwers = 9000 where age = 21;

delete from user where age = 31;

-- Changes in Table
alter table user add column city varchar(40) default "Noida";
alter table  user add column gender varchar(10) default "Unknown";
alter table user rename to insta_user;
alter table insta_user change column follwers followers int default 1000;

-- truncate basically delete data in a table and schema would exist after deletion.
truncate table user;