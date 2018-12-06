from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators

import os
import numpy as np


app = Flask(__name__)

class ReviewForm(Form):
    moviereview = TextAreaField('',
                                [validators.DataRequired(),
                                validators.length(min=15)])
@app.route('/')
def index():
    form = ReviewForm(request.form)
    return render_template('classification.html')

@app.route('/results', methods=['POST'])
def results():
    form = ReviewForm(request.form)
    if request.method == 'POST' and form.validate():
        review = request.form['moviereview']
        y = classify(review)
        z = probability(review)
        return render_template('results.html',
                                content=review,
                                prediction=y,
                                precentage=z)
    return render_template('classification.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
