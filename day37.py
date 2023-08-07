import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

df = pd.read_csv('cust_data.csv')
cal_cols = ['class', 'sex', 'stop', 'npay', 'termination', 'bill_rating']
df1 = pd.get_dummies(data=df, columns=cal_cols, drop_first=True)

X = df1.drop('termination_Y', axis=1).values
y = df1['termination_Y'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.3, 
                                                    stratify=y,
                                                    random_state=42)


df1.tail()
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
X_train[:2], y_train[:2]
X_train.shape
y_train.shape