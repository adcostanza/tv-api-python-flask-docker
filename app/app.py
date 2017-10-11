from flask import Flask, request, jsonify
from flask_restful import reqparse, Resource, Api
from show_schedule import airing_shows
app = Flask(__name__)
api = Api(app)

def options(self):
    pass
	
class Airing(Resource):
	def get(self):
		episodes = airing_shows()
		return jsonify(episodes)

api.add_resource(Airing,'/airing/')

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8080)
    