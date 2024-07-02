from flask import Flask
from flask_mysqldb import MySQL

# Initialize the Flask application
app = Flask(__name__)

# Load the configuration from config.py
app.config.from_object('config')

# Initialize MySQL with the Flask app
mysql = MySQL(app)

# Import and register the customer routes blueprint
from app.routes.customer_route import customer_bp
app.register_blueprint(customer_bp)

with app.app_context():
    db.create_all()  # This creates the tables
