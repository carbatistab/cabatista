from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'O Senhor dos Anéis - A Sociedade do Anel',
        'Autor': 'J.R.R Tolkien'
    },
    {
    'id': 2,
    'título': 'Harry Potter e a Pedra Filosofal',
    'autor': 'J.K Howling'   
    },
    {
    'id': 3,
    'títulos': 'James Clear',
    'autor': 'Hábitos Atômicos'
    },
]

@app.route('/')
def home():
    return "Para acessar o caminho, digite: /livros/id"

# Consultar (todos)
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros),200


# Consultar (id)
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        
app.run(port=200,host='localhost',debug=True)
