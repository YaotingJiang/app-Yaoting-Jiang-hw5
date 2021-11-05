from flask_mongoengine import MongoEngine
from services.dogWalkerService import init_dog_walkers

db = MongoEngine()

def initialize_db(app):
    db.init_app(app)
    init_dog_walkers()

def fetch_engine():
    return db

