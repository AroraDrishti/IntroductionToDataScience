# -*- coding: utf-8 -*-
"""Linearregression

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lVtKkwNc9fx9v6HRBEwjJWx-dWlY61QS
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# import the dataset
data = pd.read_csv("Salary_Data.csv")

data.shape

data.head()

data.info()

data.describe()

data.corr()

#Scatter Plot
plt.scatter(data['YearsExperience'], data['Salary'], alpha=0.5)
plt.title('Scatter plot of Salary with YearsExperience')
plt.xlabel('YearsExperience')
plt.ylabel('Salary')
plt.show()

#Distplot

"""Python list slicing syntax states that for a:b it will get a and everything upto but not including b. a: will get a and everything after it. :b will get everything before b but not b. The list index of -1 refers to the last element. :-1 adheres to the same standards as above in that this gets everything before the last element but not the last element. If you want the last element included use :."""

X = data.iloc[:,:-1 ].values
y = data.iloc[:,1].values

type(X)

type(y)

X.shape

y.shape

X

y

#Splitting the data set into test and training set
from sklearn.model_selection import train_test_split
X_train, X_test,y_train,y_test = train_test_split(X,y,test_size=.2,random_state=0)

# Fitting Simple Linear Regression Model to the Training Set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

A=regressor.coef_
print(A)

regressor.intercept_

# Predicting the test set results
y_pred = regressor.predict(X_test)

# Predicting the train set results
y_pred_train = regressor.predict(X_train)

y_pred

#Visualizing the training set results
plt.scatter(X_train, y_train,color ='red')
plt.plot(X_train , regressor.predict(X_train),color ='blue')
plt.xlabel('years of Experience')
plt.ylabel('salary')
plt.title('Salary Vs experience(Training Set)')
plt.show()

#Visualizing the test set results
plt.scatter(X_test, y_test,color ='red')
plt.plot(X_train , regressor.predict(X_train),color ='blue')
plt.xlabel('years of Experience')
plt.ylabel('salary')
plt.title('Salary Vs experience(Test Set)')
plt.show()

#Mean Square Error
from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, y_pred)

# Train performance
from numpy import math
math.sqrt(mean_squared_error(y_train, y_pred_train))

# Test performance
from numpy import math
math.sqrt(mean_squared_error(y_test, y_pred))

from sklearn.metrics import r2_score
r2_score(y_train, y_pred_train)

r2_score(y_test, y_pred)