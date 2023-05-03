from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error

app = Flask(_name_)
db = mysql.connector.connect(host='localhost',database='db_livros',user='roots',password='password')


@app.route('/livros', methods=['POST'])
def add_user():
    # Extract user data from request
    user_data = request.json
    numero_livro = user_data['numero_livro']
    autor = user_data['autor']
    titulo = user_data['titulo']

    # Insert the user into the database
    cursor = db.cursor()
    query = "INSERT INTO db_livros (numero_livro, titulo, autor) VALUES (%s, %s, %s)"
    values = (numero_livro, autor, titulo)
    cursor.execute(query, values)
    db.commit()
    cursor.close()

    # Return a success message
    return jsonify({'message': 'User added successfully'})
app.run(port=200,host='localhost',debug=True)
