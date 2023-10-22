#!/usr/bin/python3
""" customized results based on input """
from flask import Flask, render_template
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


@hbnb.route('/python/', strict_slashes=False)
@hbnb.route('/python/<text>', strict_slashes=False)
def python_is(text='is_cool'):
    """used to display C + inserted output"""
    return 'Python {}'.format(text.replace("_", " "))


@hbnb.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """ Display n is a number if n is an integer """
    return '{} is a number'.format(n)


@hbnb.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ returns a template displaying that the parsed arg is a number """
    return render_template('5-number.html', n=n)


@hbnb.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    if n % 2 == 0:
        number_stat = '{} is even'.format(n)
    else:
        number_stat = '{} is odd'.format(n)
    return render_template('6-number_odd_or_even.html', number_stat=number_stat)


if __name__ == '__main__':
    hbnb.run(host='0.0.0.0', port=5000)
