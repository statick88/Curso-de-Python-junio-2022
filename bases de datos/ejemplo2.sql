create database abacom;

drop database abacom;

use abacom;

create table Usuario(id int, username varchar(50), email varchar(255))

alter table Usuario add edad int;

alter table Usuario drop column edad;

alter table Usuario modify column email varchar(50)

insert into Usuario (email, username)
values ('dsaavedra88@gmail.com','statick');

delete from Usuario where email = 'dsaavedra88@gmail.com' limit 1;

alter table Usuario add primary key (id);

alter table Usuario modify column id int AUTO_INCREMENT;

insert into Usuario (email, username)
values ('juan@correo.com','juan');

insert into Usuario (email, username)
values ('pedro@correo.com','pedro');

select * from Usuario;

select * from Usuario where email = "juan@correo.com";

alter table Usuario add edad int;

select * from Usuario where edad < 30;

update Usuario set edad = 32 where id = "4";

#update Usuario set edad = 32;

delete from Usuario where id = "4";