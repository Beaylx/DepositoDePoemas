from flask import Flask, render_template

app = Flask(__name__)

poemas_data = [
    {
        "titulo": "No Meio do Caminho",
        "texto": """No meio do caminho tinha uma pedra
Tinha uma pedra no meio do caminho
Tinha uma pedra
No meio do caminho tinha uma pedra.
- Carlos Drummond de Andrade """
    },
    {
        "titulo": "Ou Isto ou Aquilo",
        "texto": """Ou isto ou aquilo
Nunca beijei ninguém
Nunca dei a mão a alguém
Sou só uma menina
Com meus versos e minha poesia.
- Cecília Meireles """
    },
    {
        "titulo": "Soneto de Fidelidade",
        "texto": """De tudo ao meu amor serei atento
Antes, e com tal zelo, e sempre, e tanto
Que mesmo em face do maior encanto
Dele se encante mais meu pensamento.
- Vinicius de Moraes """
    },
    {
        "titulo": "Ser Mulher",
        "texto": """Ser mulher é sentir o mundo inteiro
Mesmo que a vida doa
Mesmo que as palavras falhem
Mesmo que o coração chore
É carregar tudo no colo e continuar.
- Adélia Prado """
    },
    {
        "titulo": "Os Sapos",
        "texto": """Os Sapos
Os sapos, de cabeça grande, boiando no brejo
Falam, falam sem parar, entre sapos e rãs,
E eu fico a ouvir, a ouvir, e não entendo nada,
Mas gosto do canto da vida que eles entoam.
- Manuel Bandeira """
    },
    {
        "titulo": "Bilhete",
        "texto": """Se tu me amas, ama-me baixinho
Não o grites de cima dos telhados
Deixa em paz os passarinhos
Deixa em paz a mim!
Se me queres, enfim,
tem de ser bem devagarinho, Amada,
que a vida é breve, e o amor mais breve ainda...
- Mario Quintana """
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/poemas')
def poemas():
    return render_template('poemas.html', poemas=poemas_data)

if __name__ == '__main__':
    app.run(debug=True)
