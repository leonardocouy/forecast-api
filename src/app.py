import os

from flask import Flask
from flask_restful import Api

from .resources.user import User
from .resources.forecast import Forecast
from .db import db

DB_PATH = os.path.join(os.path.dirname(__file__), 'app.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:////{ DB_PATH }'
db.init_app(app)
api = Api(app)
api.add_resource(User, '/users/<user_id>')
api.add_resource(Forecast, '/users/<user_id>/forecast/<forecast_id>')


if __name__ == '__main__':
    app.run(debug=True)
