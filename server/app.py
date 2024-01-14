#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<parameter>')
def count(parameter):
    return ''.join([str(i)+'\n' for i in range(int(parameter))])

@app.route('/math/<path:parameters>')
def math(parameters):
    
    format = parameters.split('/')
    
    n1 = int(format[0])
    n2 = int(format[2])
    operation = format[1]
    
    if operation == '+':
         result = n1 + n2
    if operation == '-':
         result = n1 - n2
    if operation == '*':
         result = n1 * n2
    if operation == 'div':
         result = n1 / n2
    if operation == '%':
         result = n1 % n2
    
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)