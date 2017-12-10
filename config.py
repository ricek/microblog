import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DATABASE_URI = os.environ.get('DATABASE_URI') or \
        'mongodb+srv://kay:myRealPassword@cluster0-wpeiv.mongodb.net/test'
