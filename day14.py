import pandas as pd
import numpy as np

df=pd.read_csv("sc_cust_info_txn_v1.5.csv")
df.info()
df.head()
df.tail()
df.describe()

cust=df[["cust_class","sex_type","age","efct_svc_count","dt_stop_yn","npay_yn","r3m_avg_bill_amt","r3m_A_avg_arpu_amt","r3m_B_avg_arpu_amt", "termination_yn"]]
cust.head()

cust=cust.rename(columns = {"cust_class" : 'class',"sex_type":'sex', "efct_svc_count":'service', "dt_stop_yn":'stop',"npay_yn":'npay', "r3m_avg_bill_amt":'avg_bill', "r3m_A_avg_arpu_amt":"A_bill", "r3m_B_avg_arpu_amt":'B_bill', "termination_yn":'termination'})
cust.head()

cust.info()

cust['age'][3]+cust['age'][4]
cust=cust.astype({'age': int})
cust = cust.replace("_", np.NaN)
cust=cust.astype({'age': float })