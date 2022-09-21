# Multiple linear regression

#Importing the libraries
import numpy as np
import matplotlib.pyplot as mtp
import pandas as pd

#Importing the dataset
df = pd.read_csv('50_Startups.csv')
X = df.iloc[:,:-1]
y = df.iloc[:, 4]

#Convert the column into categorical columns
states = pd.get_dummies(X['State'],drop_first = True)

#Drop the state column
X = X.drop(X['State'],axis = 1)

#Drop the state column
