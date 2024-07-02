# Import the database object from the app module
from app import db

# Define the Customer model, which maps to the 'customer' table in the database
class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Primary key column
    name = db.Column(db.String(255), nullable=False)  # Name column, cannot be null
    age = db.Column(db.Integer, nullable=False)  # Age column, cannot be null
