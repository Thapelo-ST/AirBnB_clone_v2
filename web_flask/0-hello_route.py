#!/usr/bin/python3
""" displays hello hbnb """
from flask import Flask

hbnb = Flask(__name__)


@hbnb.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


if __name__ == '__main__':
    hbnb.run(host='0.0.0.0', port=5000)
