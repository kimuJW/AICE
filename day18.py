import pandas as pd
import numpy as np

df=pd.read_csv("sc_cust_info_txn_v1.5.csv")
cust=df[["cust_class","sex_type","age","efct_svc_count","dt_stop_yn","npay_yn","r3m_avg_bill_amt","r3m_A_avg_arpu_amt","r3m_B_avg_arpu_amt", "termination_yn"]]

cust_data['by_age']=cust_data['age']//10*10
cust_data=cust_data.astype({'age': int, 'by_age':int})

q1=cust_data['avg_bill'].quantile(0.25)
q3=cust_data['avg_bill'].quantile(0.75)
print(q1,q3)

cust_data['bill_rating'] = pd.cut(cust_data["avg_bill"], bins=[0,q1,q3,cust_data["avg_bill"].max()] , labels=['low', 'mid','high'])
cust_data.head()
print(cust_data['bill_rating'].value_counts())

cust_data['bill_rating'] = pd.qcut(cust_data["avg_bill"], 3 , labels=['low', 'mid','high'])
cust_data.head()
print(cust_data['bill_rating'].value_counts())

cust_data_num = cust_data[['avg_bill', 'A_bill', 'B_bill']]
Standardization_df = (cust_data_num - cust_data_num.mean())/cust_data_num.std()
Standardization_df.head()
Standardization_df.describe()