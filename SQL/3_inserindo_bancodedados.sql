use cadastro;

insert into usuarios
(id, nome, nascimento, sexo, peso, altura, nacionalidade)
values 
("1", "Godofredo", "1992-01-02", "M", "78.5", "1.83", "Brasil");


insert into usuarios values
(default, "Luisa", "1930-11-02", "F", "59.2","1.63", "Irlanda");

insert into usuarios values
(default, "Ana", "1924-11-02", "F", "67.9", "1.75", "Brasil"),
(default, "Marcos", "1999-10-02", "M", "99.2", "1.84", "Espanha"),
(default, "Luan","1998-12-24", "M", "76.0", "1.65", default);

select * from usuarios;