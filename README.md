
# Twitter_Sentiment_Analysis

![tweet](http://www.fuelaccounting.ca/wp-content/uploads/2015/04/twitter_logo-580-90.jpg)

Cyber bullying and hate speech has been a menace for quite a long time,So our objective for this task is to detect tweets associated with negative sentiments.
From this dataset we classify a tweet as hate speech if it has racist or sexist tweets associated with it.

So our task here is to classify racist, sexist and other offensive tweets from other tweets and filter them out.
With the given twitter dataset consisting of train.csv and test.csv files where we have 31962 labeled tweets and 17191 unlabeled tweets where we train and validate on the train.csv file and then test our best possible model on the test.csv file.

The image file present in this repository is used for super-imposing the twitter logo on the generated wordcloud.

# Summary

From the given dataset we were able to predict on which class i.e Positive or Negative does the given tweet fall into.The following data was collected from Analytics Vidhya's site.

### Dataset Description

- The data is in csv format.In computing, a comma-separated values (CSV) file stores tabular data (numbers and text) in plain text.Each line of the file is a data record. Each record consists of one or more fields, separated by commas. 
- Formally, given a training sample of tweets and labels, where label ‘1’ denotes the tweet is racist/sexist and label ‘0’ denotes the tweet is not racist/sexist,our objective is to predict the labels on the given test dataset.

### Data Pre-processing
Removing Twitter Handles(@user)
Removing puntuation,numbers,special characters
Removing short words i.e. words with length<3
Tokenization
Stemming

![pre](https://www.electronicsmedia.info/wp-content/uploads/2017/12/Data-Preprocessing.jpg)

### Data Visualisation

##### Wordclouds
WordCloud is a visualization wherein the most frequent words appear in large size and the less frequent words appear in smaller sizes

![vis](https://previews.123rf.com/images/mindscanner/mindscanner1404/mindscanner140401428/27857012-word-cloud-with-nlp-related-tags.jpg)


Barplots



### Attribute Information

- id : The id associated with the tweets in the given dataset
- tweets : The tweets collected from various sources and having either postive or negative sentiments associated with it
- label : A tweet with label '0' is of positive sentiment while a tweet with label '1' is of negative sentiment

### FEATURES

Word Embeddings used to convert words to features for our Machine Learning Model
Bag-of-Words:
Bag of Words is a method to extract features from text documents. These features can be used for training machine learning algorithms. It creates a vocabulary of all the unique words occurring in all the documents in the training set.

### TF-IDF Features (term frequency-inverse document frequency):

Tf-idf stands for term frequency-inverse document frequency, and the tf-idf weight is a weight often used in information retrieval and text mining. This weight is a statistical measure used to evaluate how important a word is to a document in a collection or corpus. The importance increases proportionally to the number of times a word appears in the document but is offset by the frequency of the word in the corpus

# Model
Machine Learning Models used: 
Logistic Regression
XGBoost
Decision Trees

# Evaluation Metrics

#### F1 score

So when we keep accuracy as our evaluation metric there may be cases where we may encounter high number of false positives.

Precison & Recall :-
Precision means the percentage of your results which are relevant.

Recall refers to the percentage of total relevant results correctly classified by your algorithmmet

![met](https://cdn-images-1.medium.com/max/800/1*pOtBHai4jFd-ujaNXPilRg.png)


We always face a trade-off situation between Precison and Recall i.e. High Precison gives low recall and vice versa.

In most problems, you could either give a higher priority to maximizing precision, or recall, depending upon the problem you are trying to solve. But in general, there is a simpler metric which takes into account both precision and recall, and therefore, you can aim to maximize this number to make your model better. This metric is known as F1-score, which is simply the harmonic mean of precision and recall.

![f1](https://cdn-images-1.medium.com/max/800/1*DIhRgfwTcxnXJuKr2_cRvA.png)


So this metric seems much more easier and convenient to work with, as you only have to maximize one score, rather than balancing two separate scores.

# Potential applications of the model:

Social media monitoring: Track public opinion and sentiment towards brands, products, or events.
Customer feedback analysis: Understand customer satisfaction and identify areas for improvement.
Political analysis: Gauge public sentiment towards candidates or policies.
Market research: Identify trends and patterns in consumer behavior.
Crisis management: Monitor public sentiment during crises and respond effectively.¶


### Visualization from Tweets

![vis](https://previews.123rf.com/images/mindscanner/mindscanner1404/mindscanner140401428/27857012-word-cloud-with-nlp-related-tags.jpg)

 WordCloud (visualization wherein the most frequent words appear in large size and the less frequent words appear in smaller sizes)



