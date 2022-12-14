import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import pickle
import streamlit as st

data = pd.read_csv("spam.csv")
print(data)
print(data.columns)
data.drop(['Unnamed: 2','Unnamed: 3','Unnamed: 4'], axis=1,inplace=True)
print(data)

data['class'] = data['class'].map({'ham': 0,'spam': 1})
print(data)

cv = CountVectorizer()

x= data['message']
y = data['class']

print(x.shape)
print(y.shape)

x = cv.fit_transform(x)
print(x)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)
print(x_train.shape)

model = MultinomialNB()

model.fit(x_train, y_train)
MultinomialNB()

result = model.score(x_test,y_test)

print(result)

msg = "Did you hear about the new"
data = [msg]
vect = cv.transform(data).toarray()
result=model.predict(vect)
print(result)
