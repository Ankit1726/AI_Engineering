-- SQL  Series Day 8 
create database restuarent;
use restuarent;

-- create table 
create table customer(
   customer_id int primary key,
   name varchar(50), 
   city varchar(50)
);

insert into customer (customer_id, name, city) values
(1, 'Alice Smith', 'New York'),
(2, 'Bob Johnson', 'Los Angeles'),
(3, 'Charlie Brown', 'Chicago'),
(4, 'Diana Prince', 'Houston'),
(5, 'Evan Wright', 'Phoenix'),
(6, 'Fiona Gallagher', 'Philadelphia'),
(7, 'George Clark', 'San Antonio'),
(8, 'Hannah Abbott', 'San Diego'),
(9, 'Ian Malcolm', 'Dallas'),
(10, 'Julia Roberts', 'San Jose');

select * from customer;

-- order table 
create table orders(
   order_id int primary key,
   customer_id int,
   dishes varchar(100),
   id_amount int 
);

insert into orders (order_id, customer_id, dishes, id_amount) values
(101, 1, 'Margherita Pizza, Garlic Bread', 450),
(102, 1, 'Chicken Alfredo Pasta, Iced Tea', 620),
(103, 2, 'Cheeseburger, French Fries, Soda', 380),
(104, 3, 'Veggie Sushi Roll, Miso Soup', 510),
(105, 4, 'Grilled Salmon, Caesar Salad', 850),
(106, 5, 'Chicken Biryani, Mango Lassi', 420),
(107, 6, 'Pepperoni Pizza, Mozzarella Sticks', 690),
(108, 7, 'Pad Thai, Spring Rolls', 480),
(109, 8, 'Steak, Mashed Potatoes', 1200),
(110, 10, 'Tacos, Churros, Lemonade', 350);

select * from orders;

-- inner join
select * from customer as c inner join orders as o 
on c.customer_id = o.customer_id;

-- left join
select * from customer as c left join orders as o 
on c.customer_id = o.customer_id;

-- right join
select * from customer as c right join orders as o 
on c.customer_id = o.customer_id;

-- cross join 
select * from 
customer cross join orders;

-- self join 
select * from customer as A join customer B 
on A.customer_id = B.customer_id;

-- Left Exclusive Joins
select * from 
customer as A
left join orders as B
on A.customer_id = B.customer_id
where B.customer_id is null;

-- Right Exclusive Joins
select * from 
customer as A
right join orders as B
on A.customer_id = B.customer_id
where A.customer_id is null;