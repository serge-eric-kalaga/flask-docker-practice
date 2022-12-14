class AppConfig():
    
    DEBUG = True
    SECRET_KEY = '0987654321'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://serge:1234@mysql_db/flask_test_db?charset=utf8mb4"
    # SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS=False