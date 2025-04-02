create sequence gerador;

select gerador.nextval from dual

create table t_cliente(
    id number,
    nome varchar2(200),
    email varchar2(100),
    documento varchar2(50),
    primary key(id));