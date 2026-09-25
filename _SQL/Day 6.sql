-- SQL  Series Day 6 

create database office; 
use office;

create table employee(
    emp_id int primary key, 
    name varchar(50), 
    department varchar(50),
    salary int,
    hire_date date
);

insert into employee (emp_id, name, department, salary, hire_date) 
values
(101, 'Alice Johnson', 'Engineering', 85000, '2021-03-15'),
(102, 'Bob Smith', 'Sales', 62000, '2019-07-22'),
(103, 'Charlie Brown', 'Marketing', 58000, '2022-01-10'),
(104, 'Diana Prince', 'Engineering', 92000, '2018-11-05'),
(105, 'Evan Wright', 'Human Resources', 54000, '2020-09-18'),
(106, 'Fiona Gallagher', 'Finance', 75000, '2017-04-12'),
(107, 'George Clark', 'Sales', 68000, '2023-02-01'),
(108, 'Hannah Abbott', 'Engineering', 88000, '2020-06-30'),
(109, 'Ian Malcolm', 'Finance', 79000, '2016-12-15'),
(110, 'Julia Roberts', 'Marketing', 61000, '2021-08-24');

select * from employee;
select name,department,salary from employee;

select * from employee where department = 'Engineering';
select distinct department from employee;
select * from employee where salary between 50000 and 80000;

select avg(salary) from employee;

select department , count(*) as employee_count 
from employee group by department having count(*) > 1;
