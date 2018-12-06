# Machine Learning Classification Project

## Authors:

`Andrea Murphy`
`Josh Quigley`

**ML**: Classification

**Subject**: COMP-840.M1

**Purpose**: Create a classification model to draw conclusion from observed values from the Adult dataset from census data

**Description**: Use classification techniques to predict what features has the most influence for having a salary over $50k/yr

**Note**: To keep the integrity of the data intact we decided to create two separate .ipynb files for the same project.

**Dataset Obtained From**:
https://archive.ics.uci.edu/ml/datasets/Adult

# Exploratory Analysis

### The Dataset
**age**​:
the age of an individual
Integer greater than 0

**workclass**​:
A general term to represent the employment status of an individual

Private, Self­emp­not­inc, Self­emp­inc, Federal­gov, Local­gov, State­gov,

Without­pay, Never­worked

**fnlwgt**​:
final weight
Integer greater than 0

**education**​:
The highest level of education achieved by an individual

Bachelors, Some­college, 11th, HS­grad, Prof­school, Assoc­acdm, Assoc­voc,

9th, 7th­8th, 12th, Masters, 1st­4th, 10th, Doctorate, 5th­6th, Preschool

**education­ num​**:
the highest level of education achieved in numerical form.
Integer greater than 0

**marital­status​**:
marital status of an individual
***Married­civ­spouse corresponds to a civilian spouse***
***Married­AF­spouse is a spouse in the Armed Forces***

Married­civ­spouse, Divorced, Never­married, Separated, Widowed, Married­spouse­absent, Married­AF­spouse

**occupation​:**
the general type of occupation of an individual
Tech­support, Craft­repair, Other­service, Sales, Exec­managerial,
Prof­specialty, Handlers­cleaners, Machine­op­inspct, Adm­clerical,
Farming­fishing, Transport­moving, Priv­house­serv, Protective­serv,
Armed­Forces

**relationship**​:
represents what this individual is relative to others
Wife, Own­child, Husband, Not­in­family, Other­relative, Unmarried

**race**​:
Descriptions of an individual’s race
White, Asian­Pac­Islander, Amer­Indian­Eskimo, Other, Black

**sex​:**
the biological sex of the individual
Male, Female

**capital­gain**​:
capital gains for an individual
Integer greater than or equal to 0

**capital­loss​:**
capital loss for an individual
Integer greater than or equal to 0

**hours­per­week​:**
the hours an individual has reported to work per week
continuous

**native­country**​:
country of origin for an individual
United­States, Cambodia, England, Puerto­Rico, Canada, Germany,
Outlying­US(Guam­USVI­etc), India, Japan, Greece, South, China, Cuba, Iran,
Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal,
Ireland, France, Dominican­Republic, Laos, Ecuador, Taiwan, Haiti, Columbia,
Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El­Salvador,
Trinadad&Tobago, Peru, Hong, Holand­Netherlands

**the label​:**
whether or not an individual makes more than $50,000 annually
<=50k, >50k

## Dataset source and content
The following is a description of our dataset:
- of Classes: 2 (‘>50K’ and ‘<=50K’)
- of attributes (Columns): 15
- of instances (Rows): 32560

## Original Data types
age                int64

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

## Classification Techniques Used
**Train the classifier**-
All classifiers in scikit-learn uses a fit(X, y) method to fit the model(training) for the given train data X and train label y.

**Predict the target**-
Given an unlabeled observation X, the predict(X) returns the predicted label y.

### Census-V1.ipynb
Decision Tree
- A model represented as a sequence of branching statements.

Support Vector Machine
 - a very powerful and versatile Machine Learning model, capable of performing linear or nonlinear classification.

Logistic Regression
- A model that generates a probability for each possible discrete label value in classification problems by applying a sigmoid function to a linear prediction.

RandomForestClassifier
- An ensemble approach to finding the decision tree that best fits the training data by creating many decision trees and then determining the average one. The random term refers to building each of the decision trees from a random selection of features, and the forest refers to the set of decision trees.

Linear SVC
- A classification algorithm that seeks to maximize the margin between positive and negative classes by mapping input data vectors to a higher dimensional space, and only supports a linear kernel.

Learning Curve
- learning curve shows how error changes as the training set size increases

## Accuracy of Models
**Education vs. Salary**-
    Decision Tree -
    Training and Testing `accuracy = 79%`

    Support Vector Machine -
    Training `accuracy = 78%` and `Testing accuracy = 79%`

    Logistic Regression-
    Training and Testing `accuracy = 78%`

**Sex vs. Salary**-
RandomForestClassifier-`Accuracy = 0.797`

### censusuClassification.ipynb
- Identifying unique categories for each feature
- Classifying the categorical features as numbers instead of their names
- Linear SVC
- Correlation Matrix

## Accuracy of Models
    Support Vector Machine for Education and Occupation-
    `accuracy = 78.7%`

    Support Vector Machine for Education and Age-
    `accuracy = 78.9%`

    Create a Support Vector Machine combining Education, age, hours.per.week, and capital.gain with income
    `accuracy = 80.2%`

### Fine Tune the Hyper-parameters:
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

## Feature engineering and feature selection
The dataset originally had a salary field that consisted of:
> <=50K and >50K

To simplify training and help to visualize the data we replaced
> <=50K with 0 and >50K with 1

For training we dropped unwanted fields and split the salary out so that we could score how accurate was the training of the model.

**Trade Offs**-
We focused on linear training a single feature. I’m sure if given more time we could improve accuracy by training with multiple features.

## Evaluate the classifier models
-  Gender has an impact whether a person will make a salary over 50K
-       More men make over 50k than women
- Education has an impact whether a person will make a salary over 50K
-       Less education a person has the less likely they will make <50K

# Conclusion

-   Men have more chances to have a higher income

-   White and Asian Pacific Islanders have more chances than other races

-   Income sort of follows the normal deviation, with a peak at 50 years old
