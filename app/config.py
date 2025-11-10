

class Config:
    API_SECRET_KEY = os.environ.get('API_SECRET_KEY')
    DEBUG = os.environ.get('DEBUG') == 'True'
    # Add other configuration variables as needed
    TESTING = os.environ.get('TESTING') == 'True'
    LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL', 'INFO')
    