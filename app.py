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

@app.route('/pokemon/mapas')
def mostra_mapa():
    reg = request.args.get("regiao").lower()

    if reg == "kanto":
        return render_template("mapas.html", mapa="http://lh5.ggpht.com/_m9vUadJLLSw/SyOTNNN56zI/AAAAAAAAAKA/OZySnnYG2hc/s640/Kantomap.png", nome = "Kanto")
    elif reg == "jhoto":
        return render_template("mapas.html", mapa="http://2.bp.blogspot.com/-FYrEe2u2eJ8/UXVs3s8uzfI/AAAAAAAAABg/nzurFet8CJc/s1600/2u3xm39.png", nome = "Jhoto")
    elif reg == "hoenn":
        return render_template("mapas.html", mapa="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/71f5d2f6-e956-4945-863c-870ebd656778/d7omhdy-db5b2226-8ab8-4c5c-93c9-73df194bafb9.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzcxZjVkMmY2LWU5NTYtNDk0NS04NjNjLTg3MGViZDY1Njc3OFwvZDdvbWhkeS1kYjViMjIyNi04YWI4LTRjNWMtOTNjOS03M2RmMTk0YmFmYjkucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.IkfpI_SXDQrTz7fXrlclqtTq3Z6vN18VfEcVgfS0b8A", nome = "Hoenn")
    elif reg == "unova":
        return render_template("mapas.html", mapa="https://gamefaqs.gamespot.com/ds/661226-pokemon-black-version-2/map/11115?raw=1", nome = "Unova")
    elif reg == "sinnoh":
        return render_template("mapas.html",mapa="https://i.pinimg.com/736x/8b/ff/3a/8bff3ab870c3e15318ded4deffe3ba79--story-ideas-maps.jpg", nome="Sinnoh")
    elif reg == "sevii islands" or reg == "ilhas sevii":
        return render_template("mapas.html",mapa="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRf0SUIiHRFlrzfpuAHznjkjc585tM9CWer0VqVxihPZbge-6dITQ3wuyEkX9qXhsnkRdI&usqp=CAU", nome="Sevii Islands")
    elif reg == "almia":
        return render_template("mapas.html", mapa="https://cdn2.bulbagarden.net/upload/f/f4/Almia.png", nome = "Almia")
    else:
        return render_template("TelaErro.html")

    #mapa_kanto= "http://lh5.ggpht.com/_m9vUadJLLSw/SyOTNNN56zI/AAAAAAAAAKA/OZySnnYG2hc/s640/Kantomap.png"
    #mapa_jhoto = "http://2.bp.blogspot.com/-FYrEe2u2eJ8/UXVs3s8uzfI/AAAAAAAAABg/nzurFet8CJc/s1600/2u3xm39.png"
    #mapa_hoenn = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/71f5d2f6-e956-4945-863c-870ebd656778/d7omhdy-db5b2226-8ab8-4c5c-93c9-73df194bafb9.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzcxZjVkMmY2LWU5NTYtNDk0NS04NjNjLTg3MGViZDY1Njc3OFwvZDdvbWhkeS1kYjViMjIyNi04YWI4LTRjNWMtOTNjOS03M2RmMTk0YmFmYjkucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.IkfpI_SXDQrTz7fXrlclqtTq3Z6vN18VfEcVgfS0b8A"



if __name__ == '__main__':
    app.run(port=80,debug=True)
