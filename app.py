from flask import Flask
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Resource, Api

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)


class EMPTY(Resource):

    def get(self):
        return "<h1>hello world</h1>"

# adding the defined resources along with their corresponding urls
api.add_resource(EMPTY, '/')

if __name__ == '__main__':
    app.run()
