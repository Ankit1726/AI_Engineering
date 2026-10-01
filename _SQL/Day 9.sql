-- SQL  Series Day 9 (Indexes In SQL)
use banK_server;

create table account_record(
    accound_id int primary key, 
    name varchar(40),
    bal decimal(10,3),
    branch_code varchar(50)
);

insert into account_record (accound_id, name, bal, branch_code) values
(101, 'Alice Smith', 1250.500, 'BR-NY-01'),
(102, 'Bob Johnson', 3400.750, 'BR-CA-02'),
(103, 'Charlie Brown', 890.200, 'BR-TX-01'),
(104, 'Diana Prince', 15200.000, 'BR-NY-01'),
(105, 'Evan Wright', 450.600, 'BR-FL-03'),
(106, 'Fiona Gallagher', 2300.850, 'BR-IL-01'),
(107, 'George Clark', 9750.125, 'BR-CA-02'),
(108, 'Hannah Abbott', 620.000, 'BR-TX-01'),
(109, 'Ian Malcolm', 11450.330, 'BR-WA-01'),
(110, 'Julia Roberts', 3100.400, 'BR-FL-03');

select * from account_record;

create index idx_branch on account_record(branch_code);
show index from account_record;

create index idx2 on account_record(branch_code,bal);
show index from account_record;
select * from account_record where branch_code = 'BR-NY-01';