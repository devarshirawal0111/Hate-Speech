#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib


# In[7]:


#X_train=X_test=Y_test=Y_train=[]


# In[8]:


def text_preprocess(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = [word for word in text.split() if word.lower() not in stopwords.words('english')]
    return " ".join(text)


# In[9]:


def train():
    #global X_train,X_test,Y_train,Y_test
    data = pd.read_csv('agr_en_train.csv')
    #X = data.text.values.tolist()
    Y = data.category.values.tolist()

    X = data['text'].copy()

    for index in range(len(Y)):
      if Y[index]=='NAG':
        Y[index]='0'
      if Y[index]=='OAG':
        Y[index]='2'
      if Y[index]=='CAG':
        Y[index]='1'
        
    X = X.apply(text_preprocess)
    
    vectorizer = TfidfVectorizer("english")
    X = vectorizer.fit_transform(X)
    
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
    
    model = LogisticRegression(multi_class="multinomial", solver="newton-cg")
    model.fit(X_train,Y_train)
    
    prediction = model.predict(X_test)
    print(accuracy_score(Y_test,prediction))
    #print(prediction[0:5])
    #print(Y_test[0:5])
    
    joblib.dump(model,'model.pkl')
    joblib.dump(vectorizer, 'vectorizer.pkl')


#train()


# In[14]:


def loadModel():
    return (joblib.load('model.pkl'), joblib.load('vectorizer.pkl'))


# In[15]:


def predict(model, data):
    #model = joblib.load('model.pkl')
    #model = loadModel()
    #prediction = model.predict(data)
    
    #print(prediction[0:5])
    return model.predict(data)
#predict(X_test)


# In[5]:





# In[ ]:




