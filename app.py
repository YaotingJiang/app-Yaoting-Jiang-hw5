from flask import Flask
from flask_restful import Api
from resources.dogWalkerResources import DogWalkerResource
from database.db import initialize_db
from utils.JSONEncoder import MongoEngineJSONEncoder


app = Flask(__name__)  # Creating a FLASK app
app.config['MONGODB_SETTINGS'] = {
    'db': 'app-yaoting-hw5',
    'host': 'mongodb://localhost:27017/app-yaoting-hw5'
}

initialize_db(app)
app.json_encoder = MongoEngineJSONEncoder
api = Api(app)

api.add_resource(DogWalkerResource,
                 '/dog_walker',
                 '/dog_walker/',
                 '/dog_walker/<string:dog_walker_id>')


@app.route('/')
def entry():
    return "APP HW5"

if __name__ == "__main__":
    app.run()