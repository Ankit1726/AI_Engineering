-- SQL  Series Day 3 

-- creating instagram database 
create database if not exists instagram;
use instagram;

-- create table 
create table user(
    id int primary key,
    age int,
    name varchar(50),
    email varchar(70) unique,
    follwers int,
    following int 
);

-- delete table in database
drop table user;

-- insert data into table (user)
insert into user (id, age, name, email, follwers, following) 
values
    (1, 24, 'John Doe', 'john.doe@example.com', 1200, 350),
    (2, 19, 'Jane Smith', 'jane.smith@example.com', 450, 180),
    (3, 31, 'Michael Brown', 'michael.b@example.com', 8900, 420),
    (4, 22, 'Emily Davis', 'emily.d@example.com', 310, 210),
    (5, 28, 'Chris Wilson', 'chris.w@example.com', 5400, 610),
    (6, 21, 'Alex Mercer', 'alex@example.com', 10000, 19),
    (7, 21, 'Bobby Vance', 'bobby@example.com', 30, 1),
    (8, 22, 'Alisha Khan', 'alisha@example.com', 789, 9);

select * from user;

-- create post table
create table post( 
    id int primary key,
    content varchar(500),
    user_id int,
    foreign key (user_id) references user(id)
);

-- insert post data
insert into post (id, content, user_id) 
values
    (101, 'Excited to announce that I starting my new journey in software engineering today!', 1),
    (102, 'Just finished reading a fantastic book on SQL database optimization. Highly recommend!', 1),
    (103, 'A beautiful sunset at the beach today. Nothing beats this view.', 2),
    (104, 'Working on a new side project using Python and React. Updates coming soon!', 3),
    (105, 'Coffee and code on a Sunday morning. The perfect routine.', 4),
    (106, 'Does anyone have recommendations for good machine learning courses?', 5),
    (107, 'Finally hit 10,000 followers! Thank you all for the support.', 6),
    (108, 'Just solved a tricky bug that took 3 hours to find. Simple typo in the end!', 8);

select * from post;

-- SQL Operarations (where caluse)
select name,age,follwers
from user where age >17 and follwers > 400;

select name,age,id
from user where age not in (16,18);

select * from user
limit 5;

-- order by clause 
select * from user order by age asc;
select * from user order by follwers desc;