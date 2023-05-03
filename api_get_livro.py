from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error

app = Flask(_name_)
db = mysql.connector.connect(host='localhost',database='db_livros',user='roots',password='password')


@app.route('/livros', methods=['GET'])
def add_user():

    cursor = db.cursor()
    cursor.execute("SELECT * FROM db_livros")
    users = cursor.fetchall()
    cursor.close()

    # Return the users as JSON
    return jsonify({'Livro cadastrados': users})
app.run(port=200,host='localhost',debug=True)
