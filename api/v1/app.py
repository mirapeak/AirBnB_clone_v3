#!/usr/bin/python3
"""
App module for init
"""
from flask import Flask, make_response, jsonify
from models import storage
import os
import sys
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.teardown_appcontext
def tearDown(self):
    """ TearDown the process """
    storage.close()


if __name__ == "__main__":
    app.run(host=os.getenv("HBNB_API_HOST"),
            port=os.getenv("HBNB_API_PORT"), threaded=True)
    sys.exit()
