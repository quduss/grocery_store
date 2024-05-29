from flask import Flask, request, jsonify
from products_dao import get_all_products
from sql_connection import get_sql_connection

app = Flask(__name__)
connection = get_sql_connection()
@app.route('/getProducts', methods=['GET'])
def get_products():
    products = get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    print("Starting Python Flask Server for Grocery Store Management System")
    app.run(port=5000)