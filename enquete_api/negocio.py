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
        ]'''
        

        




    except Exception as erro:
        traceback.print_exc()
        raise erro