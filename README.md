# Data-Mining

*Data Mining and Learning Algorithms course of the University of Patras*

In this project we use Python with Jupyter Notebook to analyze data, extract information and make predictions on the available datasets.
Those datasets are health-dataset-stroke-data.csv & spam_or_not_spam.csv, used in Task #1 and Task #2 respectively.

**Task #1:**

  * Data Analysis of the healthcare dataset regarding characteristics of 5110 unique people (extract information like range & frequency of the available characteristics, plotting-visualization of said info).
  * Data Manipulation by handling missing values with 4 different methods (drop column, fill missing values with mean column value, linear regression, k-nearest neighbors). Prepare data for the next step.
  * Use of a Random Forest Classifier on the resulting datasets to predict whether a patient is prone to having a stroke. Evaluation of the model using metrics f1score, precision and recall. Improve the results by experimenting on the input parameters.

**Task #2:**

Build a neural network that will be trained on the labeled emails dataset to predict whether an email is spam or not. At first we handle the imbalanced data of the dataset.
Since deep learning models do not understand text, we convert text into numerical representation. First we use the Tokenizer API from Tensorflow Keras, which splits sentences into words and encodes these into integers. After tokenization, we represent each sentence by sequences of numbers using texts_to_sequences() from tokenizer object. Then we pad our sequences so that each sequence will have same length. We build a sequential model with dense layer architecture and then define manually the f1, recall and precision metrics. After compiling and data fitting the model with our padded data we are ready for evaluating our model and making some predictions.
