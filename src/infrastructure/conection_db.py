from sqlalchemy import create_engine

def conect():
    BD_USER = "root"
    BD_PASS = "senhayou2up"
    BD_HOST = "35.175.45.140"
    BD_PORT = "3306"
    DATABASE = "you2up"

    SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{BD_USER}:{BD_PASS}@{BD_HOST}:{BD_PORT}/{DATABASE}"
    engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False)
    
    return engine