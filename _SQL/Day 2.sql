-- SQL Series Day 2

-- creating instagram dataase design 
create database if not exists media;
use media;

-- table schema 
create table user(
     id int,
     age int, 
     name varchar(40) not null,
     email varchar(70) unique,
     constraint age check (age>18),
     primary key (id)
);

-- insert values 
insert into user (id,age,name,email) values 
(1, 19, 'Aarav Sharma', 'aarav.sharma@example.com'),
(2, 22, 'Priya Patel', 'priya.patel@example.com'),
(3, 25, 'Rohan Verma', 'rohan.verma@example.com'),
(4, 30, 'Ananya Iyer', 'ananya.iyer@example.com'),
(5, 21, 'Kabir Mehta', 'kabir.mehta@example.com'),
(6, 28, 'Sanya Gupta', 'sanya.gupta@example.com'),
(7, 24, 'Vikram Singh', 'vikram.singh@example.com'),
(8, 20, 'Neha Reddy', 'neha.reddy@example.com'),
(9, 35, 'Aditya Joshi', 'aditya.joshi@example.com'),
(10, 27, 'Diya Sen', 'diya.sen@example.com');

select * from user;
select distinct age from user;

-- media data 
create table post(
   id int primary key, 
   content varchar(400), 
   user_id int,
   foreign key (user_id) references user(id)
);

INSERT INTO post (id, content, user_id) VALUES
(101, 'Excited to start learning SQL today!', 1),
(102, 'Just finished a great workout session. Feeling energized!', 3),
(103, 'Does anyone have good book recommendations for software design?', 2),
(104, 'Coffee and code on a Sunday morning. ☕💻', 1),
(105, 'Loving the autumn weather outside today.', 5),
(106, 'Working on a new web app project using React and PostgreSQL.', 4),
(107, 'Attended a fantastic tech meetup evening!', 2),
(108, 'Exploring new hiking trails over the weekend.', 3);

select*from post;
show databases;