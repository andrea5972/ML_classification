# Machine Learning Classification Project

## Authors:

`Andrea Murphy`
`Josh Quigley`

**ML**: Classification
**Subject**: COMP-840.M1
**Purpose**: Create a classification model to draw conclusion from observed values from the Adult dataset from census data.
**Description**: Use classification techniques to predict what features has the most influence for having a salary over $50k/yr.
- Education vs Salary
- Sex vs Salary

**Dataset Obtained From**:
https://archive.ics.uci.edu/ml/datasets/Adult

## Dataset source and content
The following is a description of our dataset:
- of Classes: 2 (‘>50K’ and ‘<=50K’)
- of attributes (Columns): 15
- of instances (Rows): 32560

## Original Data types
>age                int64
workclass         object
fnlwgt             int64
education         object
education-num      int64
marital-status    object
occupation        object
relationship      object
race              object
sex               object
capital-gain       int64
capital-loss       int64
hours-per-week     int64
native-country    object
salary             int64

dtypes: int64(7), object(8)

## Classification Techniques
**Education vs. Salary**-
Decision Tree - A model represented as a sequence of branching statements.
Support Vector Machine - a very powerful and versatile Machine Learning model,  capable of performing linear or nonlinear classification.
Logistic Regression - A model that generates a probability for each possible discrete label value in classification problems by applying a sigmoid function to a linear prediction.

**Sex vs. Salary**-
1-hot encoding to categorical feature “sex”
data_sex = pd.get_dummies(data_sex, columns=['sex'], prefix
= ['sex'])

**Initialize the classifier**-
RandomForestClassifier
Linear SVC and Learning Curve
Train the classifier-
All classifiers in scikit-learn uses a fit(X, y) method to fit the model(training) for the given train data X and train label y.

**Predict the target**-
Given an unlabeled observation X, the predict(X) returns the predicted label y.
predictions = clf.predict(X_test)
print(accuracy_score(y_test, predictions))
**Evaluate the classifier model**-
-  Gender has an impact whether a person will make a salary over 50K
-       More men make over 50k than women
- Education has an impact whether a person will make a salary over 50K
-       Less education a person has the less likely they will make <50K

## Models
### Trade Offs-
**Education vs. Salary**-
Decision Tree - Trade off is it can overfit if the tree grows too deep.
Support Vector Machine - Trade off is it’s slower than other classifiers.
Logistic Regression - Trade off is it underperforms in nonlinear training scenarios.

### Fine Tune the Hyper-parameters:
**Education vs. Salary**-
Decision Tree
- Random State
    - to train with the same random data each time.

Max Depth
-  to limit the tree from overfitting the training data.

Min Samples Leaf
- guaranteeing more samples at each leaf

Support Vector Machine
- Random State
  - To train with the same random data each time
  - Kernel - RBF had the best results

Logistic Regression
- Random State
    - To train with the same random data each time.
- Solver
    - liblinear used for small linear datasets.

### Accuracy of Models

**Education vs. Salary**-
    Decision Tree -
    Training and Testing `accuracy = 79%`
    Support Vector Machine -
    Training `accuracy = 78%` and `Testing accuracy = 79%`
    Logistic Regression-
    Training and Testing `accuracy = 78%`

**Sex vs. Salary**-
RandomForestClassifier-
`Accuracy = 0.797`

## Feature engineering and feature selection
The dataset originally had a salary field that consisted of:
> <=50K and >50K

To simplify training we replaced
> <=50K with 0 and >50K with 1

This also helped with visualizing the data.
We did not have any nulls to contend with in our dataset.
For training we dropped unwanted fields and split the salary out so that we could score how accurate was the training of the model.
**Trade Offs**-
We focused on linear training a single feature. I’m sure if given more time we could improve accuracy by training with multiple features.

