import negocio
from flask import Flask, jsonify, request
import traceback

app = Flask(__name__)

@app.route("/partidas", methods=['GET'])
def hello():
    return ({"msg": "hello"}, 200)

@app.route("/times", methods=['GET'])
def recupera_times():
    try:
        dados = negocio.recupera_times()
        return (dados, 200)
    except Exception as erro:
        traceback.print_exc()
        info = {'title': str(erro), 'status': 400}
        return (info, 400)


@app.route("/partidas", methods=["POST"])
def insere_partida():
    partida = request.json
    try:
        negocio.cadastra_partida(partida)
        return (jsonify(partida), 201)
    except Exception as e:
        #print(e)
        traceback.print_exc()
        info = {"msg": "Time não encontrado", "status": 400}
        return (jsonify(info), 400)

app.run(debug=True)
