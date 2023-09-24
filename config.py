import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://test_t7rg_user:9PB6Yz2ZdSAGbSVu3fOJkFaQbwfEWxVo@dpg-ck7tbh7sasqs73cc6smg-a.singapore-postgres.render.com/test_t7rg'

class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')