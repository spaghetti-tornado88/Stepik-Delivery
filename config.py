import os

class Config:
    SECRET_KEY = os.urandom(8)
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@127.0.0.1:5432/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False