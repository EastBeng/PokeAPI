from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def carregaTela():  # put application's code here
    return render_template("index.html")

@app.route('/pokemon')
def pokemon():
    try:
        poke = request.args.get("busca").lower()

        url = "https://pokeapi.co/api/v2/pokemon/{}".format(poke)
        i = 1
        response = requests.get(url)
        resposta = response.json()

        url2 = resposta['location_area_encounters']
        response2 = requests.get(url2)
        resposta2 = response2.json()

        return render_template("buscaPoke.html", resp=resposta, nome_poke=poke.upper(), resp2=resposta2)

    except:

        return render_template("TelaErro.html")

@app.route('/pokemon/mapa')
def mostra_mapa():
    mapa_kanto= "https://lh6.googleusercontent.com/proxy/yCPrYBpUuJTo3jS9glluiqTcrMoJhURNcArVydwkUBAEatTQj9TRCHg9mPo3U3zrtvl1w2xcFJ8kXzeYLmdQyP1p3oJTpUa9KA=s0-d"


if __name__ == '__main__':
    app.run(port=80,debug=True)
