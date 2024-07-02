from flask import Blueprint, jsonify, request
from app import mysql

# Create a Blueprint for customer routes
customer_bp = Blueprint('customer', __name__)

# Route to add a new customer
@customer_bp.route('/data', methods=['POST'])
def add_data():
    cur = mysql.connection.cursor()
    name = request.json['name']
    age = request.json['age']
    cur.execute('''INSERT INTO customer (name, age) VALUES (%s, %s)''', (name, age))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Data added successfully'})

# Route to get all customers
@customer_bp.route('/data', methods=['GET'])
# def get_data():
#     cur = mysql.connection.cursor()
#     cur.execute('''SELECT * FROM customer''')
#     data = cur.fetchall()
#     print(data)
#     cur.close()
#     return jsonify(data)

def get_data():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM customer''')
    rows = cur.fetchall()
    
    # Get column names from cursor description
    column_names = [desc[0] for desc in cur.description]
    
    # Convert rows into a list of dictionaries
    data = [dict(zip(column_names, row)) for row in rows]
    
    cur.close()
    return jsonify(data)

# Route to get a specific customer by ID
@customer_bp.route('/data/<int:id>', methods=['GET'])
def get_data_by_id(id):
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM customer WHERE id = %s''', (id,))
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

# Route to update a customer by ID
@customer_bp.route('/data/<int:id>', methods=['PUT'])
def update_data(id):
    cur = mysql.connection.cursor()
    name = request.json['name']
    age = request.json['age']
    cur.execute('''UPDATE customer SET name = %s, age = %s WHERE id = %s''', (name, age, id))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Data updated successfully'})

# Route to delete a customer by ID
@customer_bp.route('/data/<int:id>', methods=['DELETE'])
def delete_data(id):
    cur = mysql.connection.cursor()
    cur.execute('''DELETE FROM customer WHERE id = %s''', (id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Data deleted successfully'})
