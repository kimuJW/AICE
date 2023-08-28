import pandas as pd
import numpy as np

df = pd.read_csv("onenavi_train.csv", sep="|")
df

df = pd.read_csv("onenavi_train.csv",sep="|")
df_eval = pd.read_csv("onenavi_evaluation.csv",sep="|")
df_total=pd.concat([df,df_eval],ignore_index=True)
df_total

df_pnu = pd.read_csv("onenavi_pnu.csv",sep="|") 
df_signal = pd.read_csv("onenavi_signal.csv",sep="|") 

df_total=pd.merge(df_total,df_pnu , on="RID")
df_total=pd.merge(df_total,df_signal , on="RID")
df_total