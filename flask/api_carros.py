from flask import Flask, jsonify, request
import db

#app = Flask(__name__)
app = Flask("API de Carros")

#área para a criação das funções

#definindo URL e método para chamar a funcao
@app.route("/hello", methods=["GET"]) 
def get_hello():
    resp = {
        "msg": "Hello World!"
    }
    #sempre vamos devolver uma tupla
    return (jsonify(resp), 200)
    #200 representa o HttpStatusCode ok (deu certo)


@app.route("/carros", methods=["GET"])
def get_all_cars():
    return (jsonify(db.carros), 200)

#http://127.0.0.1:5000/carros/4
#quero definir uma URL que permita recuperar apenas um carro da base
#passo o id do carro na URL e recebo o carro de volta
@app.route("/carros/<int:id>", methods=['GET']) #definir rotas faz a ligacao entre a URL e a funcao python
def get_car_by_id(id: int):
    for carro in db.carros:
        if carro['id'] == id:
            return (jsonify(carro), 200)
        
    info = {
        "msg": f"Nenhum carro com id={id} encontrado",
        "status": 404
    }
    return (jsonify(info), 404)


@app.route("/carros/montadora/<string:montadora>", methods=['GET'])
def get_cars_by_montadora(montadora: str):
    resp = []
    for carro in db.carros:
        if carro['montadora'] == montadora:
            resp.append(carro)
    
    if len(resp) > 0:
        return (jsonify(resp), 200)
    else:
        info = {"msg": "Nenhum carro encontrado", "status": 404}
        return (jsonify(info), 404)

@app.route("/carros", methods=['POST'])
def insert_car():
    carro = request.json #pegando o carro que sera inserido no banco
    for i in range(len(db.carros)):
        c = db.carros[i]
        if c['id'] == carro['id']:
            info = {"msg": "Já existe carro com o mesmo id", 
                    "status": 406}
            return (info, 406)
    
    db.carros.append(carro)
    return (jsonify(carro), 201)





app.run(debug=True)