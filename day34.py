import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cust_data.csv')
df.info()
df.tail()
df['termination'].value_counts().plot(kind='bar')