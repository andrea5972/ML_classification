# ML: Regression

Author: `Andrea Murphy` and `Josh Quigley`

Subject: COMP-840.M1

Purpose: Create a regression model based on news popularity in multiple social media platforms.

Dataset:

[https://archive.ics.uci.edu/ml/datasets/News+Popularity+in+Multiple+Social+Media+Platforms](https://archive.ics.uci.edu/ml/datasets/News+Popularity+in+Multiple+Social+Media+Platforms)

# Dataset source and content-

**Data types:**
RangeIndex: 93239 entries, 0 to 93238
Data columns (total 11 columns):
IDLink 93239 non-null float64
Title 93239 non-null object
Headline 93224 non-null object
Source 92960 non-null object
Topic 93239 non-null object
PublishDate 93239 non-null object
SentimentTitle 93239 non-null float64
SentimentHeadline 93239 non-null float64
Facebook 93239 non-null int64
GooglePlus 93239 non-null int64
LinkedIn 93239 non-null int64
dtypes: float64(3), int64(3), object(5)
memory usage: 7.8+ MB

# Exploratory Analysis

**The Dataset**

IDLink (numeric): Unique identifier of news items

Title (string): Title of the news item according to the official media sources

Headline (string): Headline of the news item according to the official media sources

Source (string): Original news outlet that published the news item

Topic (string): Query topic used to obtain the items in the official media sources

PublishDate (timestamp): Date and time of the news items' publication

SentimentTitle (numeric): Sentiment score of the text in the news items' title

SentimentHeadline (numeric): Sentiment score of the text in the news items' headline

Facebook (numeric): Final value of the news items' popularity according to the social media source Facebook

GooglePlus (numeric): Final value of the news items' popularity according to the social media source Google+

LinkedIn (numeric): Final value of the news items' popularity according to the social media source LinkedIn

## Feature Engineering

We parsed the Time out of the PublishDate field using pd.to_datetime, we then converted the Time field into Minutes as a float is required to train.

## Regression Techniques

Linear Regression - A regression model that outputs a continuous value from a linear combination of input features.

Lasso Regression - Least Absolute Shrinkage and Selection Operator Regression is another regularized form of Linear Regression.

Ridge Regression - a regularized form of Linear Regression.

## Models

Trade Off-

The PublishDate field contains both the date and the time, this makes it difficult to use. With more time we would have explored parsing out the date and the time into separate fields so then it could be used to help visualize the data and train. Specifically, looking at what time of day results in the most popular stories on social media.

## Tune the hyper-parameters
Random_state reproduces the same sequence of random numbers for comparing identical training sessions.

Alpha - a positive integer that defines the strength of the regularization.

Solver - saga uses an improved version of the Stochastic Average Gradient Descent.

Max_iter - preset for the maximum number of iterations .

# Accuracy of Models:

Facebook & GooglePlus - We see that as the Facebook popularity increases for a given new story there is a correlation with a gradual increase in the GooglePlus popularity.


Facebook & SentimentHeadline - We see that Facebook popularity has very little correlation with the perceived sentiment of a news story headline.


Time of Day & Facebook - Linear Regression shows that generally later in the day results in more popular news stories.

# Conclusion

-   Facebook Popularity can be vaguely predict popularity on other social media platforms, in this case GooglePlus

-   Facebook Popularity does not correlate nor predict SentimentHeadline scores

-   Publishing Later in the day tends to lead towards more popularity on Facebook

-   This was a challenging dataset and probably not the best choice for Regression
