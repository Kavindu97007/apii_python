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
