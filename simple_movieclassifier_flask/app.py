from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators
import pickle
import os
import numpy as np

# import HashingVectorizer from local dir
from vectorizer import vect

app = Flask(__name__)

######## Preparing the Classifier
cur_dir = os.path.dirname(__file__)
clf = pickle.load(open(os.path.join(cur_dir,
                 'pkl_objects',
                 'classifier.pkl'), 'rb'))

def classify(document):
    label = {0: 'negative', 1: 'positive'}
    X = vect.transform([document])
    y = clf.predict(X)[0]
    return label[y]

def probability(document):
    X = vect.transform([document])
    z = np.max(clf.predict_proba(X)) * 100
    return round(z, 2)

######## Flask
class ReviewForm(Form):
    moviereview = TextAreaField('',
                                [validators.DataRequired(),
                                validators.length(min=15)])

@app.route('/')
def index():
    form = ReviewForm(request.form)
    return render_template('reviewform.html', form=form)

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
    return render_template('reviewform.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
