import pandas as pd
import numpy as np

df=pd.read_csv("sc_cust_info_txn_v1.5.csv")
cust=df[["cust_class","sex_type","age","efct_svc_count","dt_stop_yn","npay_yn","r3m_avg_bill_amt","r3m_A_avg_arpu_amt","r3m_B_avg_arpu_amt", "termination_yn"]]

cust=cust.fillna(15)
cust.head()
cust.info()

cust=cust_fix.copy()
cust=cust.fillna(method='backfill')
cust.head()

cust=cust_fix.copy()
cust=cust.fillna(method='ffill')
cust.head()

cust=cust_fix.copy()
cust['age']=cust['age'].replace(np.nan, cust['age'].median())
cust.head()

cust=cust_fix.copy()
cust=cust.interpolate()
cust.head()