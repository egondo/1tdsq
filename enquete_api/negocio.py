import banco
import traceback

def recupera_perguntas(enquete: int) -> list:
    try:
        perguntas = banco.recupera_perguntas(enquete)
        #Queremos que os dados aparecam da seguinte forma:
        '''[
            {"id": 1, "numero": 1, "questao": "Qual time torce?", 
             "tipo": "aberta", "itens": []},
            {"id": 2, "numero": 2, "questao": "Quem vai ganhar?",
            "tipo": "unica", "itens": ["Barcelona", "Inter", ...]}
        ]
        (1, 1, 'Qual o time que você torce?', 'aberta', None)
        (2, 2, 'Quem vai ganhar a Champions?', 'unica', 'Barcelona')
        (2, 2, 'Quem vai ganhar a Champions?', 'unica', 'PSG')
        (2, 2, 'Quem vai ganhar a Champions?', 'unica', 'Arsenal')
        '''
        colecao = []
        aux_id = -1
        registro = None
        for dado in perguntas:
            if aux_id != dado[0]:
                aux_id = dado[0]
                if registro != None:
                    colecao.append(registro)
                registro = {
                    "id": dado[0], "numero": dado[1],
                    "questao": dado[2], "tipo": dado[3],
                    "itens": []
                }
            registro['itens'].append(dado[4])
        colecao.append(registro)
        return colecao
    except Exception as erro:
        traceback.print_exc()
        raise erro
    

def cadastra_respostas(dados):
    try:
        usuario = None
        i = 0
        while i < len(dados):
            if int(dados[i]['id']) == 0:
                usuario = dados[i]['valor']
                dados.pop(i)
                break
            i = i + 1

        print(usuario, dados)
        banco.inclui_respostas(dados, usuario)
    except Exception as erro:
        traceback.print_exc()
        raise erro

if __name__ == "__main__":
    dados = recupera_perguntas(1)
    for reg in dados:
        print(reg)