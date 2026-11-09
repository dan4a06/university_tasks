create table afanasiev342.supplier (
	supplier_ID integer primary key,
	supplier_name varchar(20) not null,
	city varchar(20) not null,
	unique(supplier_name, city)
);

create table afanasiev342.part (
	part_ID integer primary key,
	part_name varchar(20) not null,
	price decimal(5, 2) check(price > 0) not null,
	weight decimal(5, 2) check(weight > 0) not null,
	color char check(color in ('R', 'G', 'B')) not null,
	unique(part_name, price, weight, color)
);

create table afanasiev342.sells (
	sells_ID integer primary key,
	supplier_ID integer references afanasiev342.supplier on update cascade on delete set null,
	part_ID integer not null references afanasiev342.part on update cascade on delete cascade,
	unique(supplier_ID, part_ID)
);

insert into afanasiev342.supplier(supplier_ID, supplier_name, city)
	values
		(1, 'Smith', 'London'),
		(2, 'Jones', 'Paris'),
		(3, 'Adams', 'Vienna'),
		(4, 'Blake', 'Rome');

insert into afanasiev342.part (part_ID, part_name, price, weight, color)
	values
		(1, 'Screw', 10, 2, 'R'),
		(2, 'Nut', 8, 4, 'G'),
		(3, 'Bolt', 15, 5, 'B'),
		(4, 'Cam', 25, 3, 'R'),
		(5, 'Bering', 40, 7, 'B');

insert into afanasiev342.sells (sells_ID, supplier_ID, part_ID)
	values
		(1, 1, 1),
		(2, 1, 2),
		(3, 2, 4),
		(4, 3, 1),
		(5, 3, 3),
		(6, 3, 5),
		(7, 4, 2),
		(8, 4, 3),
		(9, 4, 4),
		(10, 2, 5)

select * from afanasiev342.supplier

select * from afanasiev342.part

select * from afanasiev342.sells

