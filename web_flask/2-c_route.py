#!/usr/bin/python3
""" displays C and inserted input """
from flask import Flask

hbnb = Flask(__name__)


@hbnb.route('/', strict_slashes=False)
def hello():
    """ function for displaying hello hbnb """
    return 'Hello HBNB!'


@hbnb.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """used to display hbnb"""
    return 'HBNB'


@hbnb.route('/c/<text>', strict_slashes=False)
def c_is(text):
    """used to display C + inserted output"""
    return 'C {}'.format(text.replace("_", " "))


if __name__ == '__main__':
    hbnb.run(host='0.0.0.0', port=5000)
