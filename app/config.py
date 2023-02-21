import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    """Base Config Object"""
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY', '!nfo3180L@b3')
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'sandbox.smtp.mailtrap.io')
    MAIL_PORT = os.environ.get('MAIL_PORT', '2525')
    MAIL_USERNAME = os.environ.get('262bf58a4439a4')
    MAIL_PASSWORD = os.environ.get('7f3b0ff56553fd')
