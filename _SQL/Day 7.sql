-- SQL  Series Day 7 

create database bank_server;
use bank_server;

create table accounts(
    id int primary key, 
    name varchar(50), 
    balance decimal(10,3)
);

INSERT INTO accounts (id, name, balance) VALUES
(101, 'Ankit Gupta', 86856.480),
(102, 'Ankita Sharma', 68564.800),
(103, 'Kush Patel', 85648.250),
(104, 'Rohan Verma', 12450.500),
(105, 'Priya Singh', 94320.750),
(106, 'Amit Kumar', 31200.000),
(107, 'Sneha Reddy', 50450.125),
(108, 'Vikram Malhotra', 115000.900),
(109, 'Neha Joshi', 27800.330),
(110, 'Rahul Mehta', 64300.600);

select * from accounts;

-- Transactions 
select @@autocommit;
set autocommit = 0;

start transaction;
update accounts set balance = balance + 1056445 where id = 101;
update accounts set balance = balance - 40066 where id = 102;
commit;

-- after commit rollback not possible
rollback;

-- savepoint 
update accounts set balance = balance + 53532 where id = 101;

savepoint wallet_topup;
update accounts set balance = balance + 5000 where id = 101;
commit;

-- error 
rollback to wallet_topup;