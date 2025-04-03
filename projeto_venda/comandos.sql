create sequence gerador;

select gerador.nextval from dual

create table t_cliente(
    id number,
    nome varchar2(200),
    email varchar2(100),
    documento varchar2(50),
    primary key(id));

create table t_venda(
    id number,
    data date,
    valor number(8, 2),
    id_cliente number,
    primary key(id),
    foreign key(id_cliente) references t_cliente(id)
);    

create table t_itemvenda(
    produto varchar2(100),
    quantidade number,
    valor number(8, 2),
    id_venda number,
    foreign key(id_venda) references t_venda(id)
);
