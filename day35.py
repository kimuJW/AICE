import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cust_data.csv')
cal_cols = ['class', 'sex', 'stop', 'npay', 'termination', 'bill_rating']
df1 = pd.get_dummies(data=df, columns=cal_cols, drop_first=True)
df1.info()