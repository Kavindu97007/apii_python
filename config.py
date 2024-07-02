# Configuration settings for the Flask application

class Config:
    # Database connection settings
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'root'
    MYSQL_DB = 'restaurant_db2'
    MYSQL_CURSORCLASS = 'DictCursor'  # Use DictCursor to return results as dictionaries

# Initialize the configuration
app_config = Config()


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'restaurant_db'
mysql = MySQL(app)
