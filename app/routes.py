from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators
import pickle
import os
import numpy as np

app = Flask(__name__)

# two decorators, same function
@app.route('/')
def index():
    return render_template('index.html', the_title='Income-o-Meter')

if __name__ == '__main__':
    app.run(debug=True)
