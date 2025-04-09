import banco

def cadastra_venda ( cliente : dict , venda : dict ):
    cli = banco.recupera_cliente_documento(cliente['documento'])
    if not cli:
        banco.insere_cliente(cliente)
        venda['id_cliente'] = cliente ['id']
    else :
        venda ['id_cliente'] = cli [0]
    itens_venda = venda ['itens']
    venda.pop('itens')
    banco.insere_venda(venda)
    idvenda = venda['id']
    for iv in itens_venda:
        iv ['id_venda'] = idvenda
        banco.insere_itemvenda ( iv )

if __name__ == "__main__":
    cliente = {
        'documento': '324.503.928-85',
        'nome': 'Fernando Gomes',
        'email': 'fefe@fiap.com.br'
    }

    venda = {
        'data': '03-04-2025',
        'valor': 2500,
        'itens': [
            {'produto': 'lapis',
              'quantidade': 1000,
              'valor': 0.50
            },
            {'produto': 'borracha',
            'quantidade': 2000,
            'valor': 1.00}
        ]
    }

    cadastra_venda(cliente, venda)