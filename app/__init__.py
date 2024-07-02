from flask import Flask
from flask_mysqldb import MySQL
#from config import Config 

# Initialize the Flask application
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'restaurant_db'
mysql = MySQL(app)

# Load the configuration from config.py
#app.config.from_object(Config)

# Initialize MySQL with the Flask app
#mysql = MySQL(app)

# Import and register the customer routes blueprint
from app.routes.customer_route import customer_bp
app.register_blueprint(customer_bp)

# with app.app_context():
#     db.create_all()  # This creates the tables
