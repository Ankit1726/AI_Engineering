-- SQL Learning Series Day 1 

-- creating database 
create database college;
use college;

create table student(
    roll int, 
    name varchar(50),
    age int 
);

INSERT INTO student (roll, name, age) VALUES
(101, 'Aarav Sharma', 20),
(102, 'Priya Patel', 21),
(103, 'Rohan Verma', 19),
(104, 'Ananya Iyer', 22),
(105, 'Kabir Mehta', 20),
(106, 'Sanya Gupta', 21),
(107, 'Vikram Singh', 23),
(108, 'Neha Reddy', 19),
(109, 'Aditya Joshi', 20),
(110, 'Diya Sen', 22);

select * from student;
show databases;