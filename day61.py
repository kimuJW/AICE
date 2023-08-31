import pandas as pd
import numpy as np

df = pd.read_csv("onenavi_train.csv",sep="|")
df_eval = pd.read_csv("onenavi_evaluation.csv",sep="|")
df

df_total=pd.concat([df,df_eval],ignore_index=True)
df_total.isnull().sum()

sample = pd.DataFrame(
        {
            'column1':[50,70,np.nan,55],
            'column2':[22,50,66,np.nan]
        })
sample

sample.dropna()
sample.fillna(0)
sample.fillna(method='pad')