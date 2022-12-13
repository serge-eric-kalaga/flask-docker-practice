class AppConfig():
    
    DEBUG = True
    SECRET_KEY = '0987654321'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://flask_user:1234@localhost/flask_test_db?charset=utf8mb4"
    # SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS=False