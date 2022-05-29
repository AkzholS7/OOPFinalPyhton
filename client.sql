create table client (
	id serial PRIMARY KEY,
	client_name VARCHAR(50) NOT NULL,
	food_name VARCHAR(50) NOT NULL,
	price VARCHAR(50) NOT NULL,
	amount INT,

);
insert into client(id, client_name, food_name, price, amount) values (1, 'Isidro', 'Randales', '$1.86', 42);
insert into client(id, client_name, food_name, price, amount) values (2, 'Raf', 'Wilcockes', '$1.47', 8);
insert into client(id, client_name, food_name, price, amount) values (3, 'Angel', 'Sprake', '$3.94', 84);

--we need this to alter sequence, it will help you to add info to DB
alter sequence client_id_seq restart with 9