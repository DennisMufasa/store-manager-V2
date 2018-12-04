"""Application configuration"""
# system import
import os

class Configure:
    """Parent config class"""
    DEBUG = False
    POSTGRES_DATABASE_URI = os.getenv('DATABASE_URI')


class Development(Configure):
    """Development configurations"""
    DEBUG = True


class Testing(Configure):
    """Testing configurations"""
    DEBUG = True
    TESTING = True
    POSTGRES_DATABASE_URI = 'postgresql://localhost/test_db'


configure = {
    "development" : Development,
    "testing" : Testing
}
