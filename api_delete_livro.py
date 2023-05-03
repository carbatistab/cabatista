from flask import Flask, jsonify, request
import mysql.connector

app = Flask(_name_)
db = mysql.connector.connect(host='localhost',database='db_livros',user='roots',password='password')

# Define route to delete a book
@app.route('/livros/<numero_livro>', methods=['DELETE'])
def delete_book(numero_livro):
    cursor = db.cursor()
    cursor.execute("DELETE FROM db_livros WHERE numero_livro")
    db.commit()
    return jsonify({'message': 'Book deleted successfully.'})

app.run(port=200,host='localhost',debug=True)
