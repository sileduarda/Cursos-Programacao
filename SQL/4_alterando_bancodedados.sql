use cadastro;

desc usuarios; 

alter table usuarios
add column profissao varchar(10);

select * from usuarios;

alter table usuarios
drop column profissao;

alter table usuarios
add column profissao varchar(10) after nome;

alter table usuarios
add column codigo int first;

alter table usuarios
modify column profissao varchar (20) not null default '';

alter table usuarios
change column profissao prof varchar (20) not null default '';

alter table usuarios
rename to gafanhotos;

alter table gafanhotos 
rename to usuarios;

use cadastro; 

create table if not exists cursos (
nome varchar (30) not null unique, 
descricao text,
carga int unsigned,
totaulas int unsigned,
ano year default '2016'
) default charset = utf8mb4;

alter table cursos
add column idcurso int first;

alter table cursos
add primary key (idcurso);

desc cursos;

