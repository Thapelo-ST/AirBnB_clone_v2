#!/usr/bin/python3
""" displays hbnb """
from flask import Flask

hbnb = Flask(__name__)


@hbnb.route('/hbnb', strict_slashes=False)
def hbnb():
    """used to display hbnb"""
    return 'HBNB'


if __name__ == '__main__':
    hbnb.run(host='0.0.0.0', port=5000)
