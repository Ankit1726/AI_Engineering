-- SQL  Series Day 9 (Stored Procedure)

use bank_server;
select * from accounts;

-- Stored Procedure
delimiter $$

create procedure check_bal(in acc_id int)
begin 
     select balance
     from accounts
     where id = acc_id;
end $$
call check_bal(101);

-- Stored Procedure
delimiter $$

create procedure check_bal(in acc_id int,out bal decimal(10,2))
begin 
     select balance into bal
     from accounts
     where id = acc_id;
end $$

delimiter ;

call check_bal(102,@balance);
select @balance;

drop procedure if exists check_bal;