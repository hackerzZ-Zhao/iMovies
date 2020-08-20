
from config.base_setting import *

SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@35.235.72.245/iMovies'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = '321'

DOMAIN = {
    'www': 'http://35.235.72.245:80'
}

#RELEASE_PATH = '/Users/zhaoziwei/PycharmProjects/Movies/iMovies/project/release_version'