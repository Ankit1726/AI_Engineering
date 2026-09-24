-- SQL  Series Day 5 

create database university;
use university;

create table Professor(
    id int primary key, 
    name varchar(50) not null,
    subject varchar(20),
    salary int default 40000
);

insert into Professor (id, name, subject, salary) values
(1, 'Dr. Alan Turing', 'Computer Science', 75000),
(2, 'Dr. Marie Curie', 'Physics', 80000),
(3, 'Dr. Ada Lovelace', 'Mathematics', 70000),
(4, 'Dr. Richard Feynman', 'Physics', 65000),
(5, 'Dr. Grace Hopper', 'Computer Science', 40000),
(6, 'Dr. Kaveri', 'Computer Science',45000); 
select * from Professor;

-- Table Queries 
set sql_safe_updates = 0;
alter table Professor change column salary ctc int;

-- add bonus 
update Professor set ctc = ctc+ctc*0.45;
alter table Professor rename to University_Employee;

select * from University_Employee;
alter table University_Employee add column city varchar(40) default "Gurgoan";
update  University_Employee set city = "Noida" where id > 3;
