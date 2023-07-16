import pandas as pd
import numpy as np

df=pd.read_csv("sc_cust_info_txn_v1.5.csv")
cust=df[["cust_class","sex_type","age","efct_svc_count","dt_stop_yn","npay_yn","r3m_avg_bill_amt","r3m_A_avg_arpu_amt","r3m_B_avg_arpu_amt", "termination_yn"]]

cust=cust_fix.copy()
cust=cust.dropna()
cust.info()

cust=cust_fix.copy()
cust=cust.dropna(how='all')
cust.info()

cust=cust_fix.copy()
cust[['npay','stop','termination']]=cust[['npay','stop','termination']].replace('N', np.nan)
cust[['service','avg_bill','A_bill','B_bill']]=cust[['service','avg_bill','A_bill','B_bill']].replace(0, np.nan)
cust=cust.dropna(how='all')
cust[['npay','stop','termination']]=cust[['npay','stop','termination']].replace(np.nan,'N')
cust[['service','avg_bill','A_bill','B_bill']]=cust[['service','avg_bill','A_bill','B_bill']].replace(np.nan, 0)
cust.info()

cust=cust_fix.copy()
cust[(cust['avg_bill']==0)]

cust=cust_fix.copy()
cust=cust.dropna(thresh=10)
cust.info()

cust=cust_fix.copy()
cust=cust.dropna(subset=['class'])
cust.info()