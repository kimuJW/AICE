import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

df_feature = pd.read_csv("onenavi_train_feature.csv",sep="|")
df_target = pd.read_csv("onenavi_train_target.csv",sep="|")

train_x, test_x, train_y, test_y = train_test_split(df_feature, df_target, test_size=0.20, random_state=42)