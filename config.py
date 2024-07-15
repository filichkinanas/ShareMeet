import os


base_dir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'sqlite:///' + os.path.join(base_dir, 'comments.db')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'