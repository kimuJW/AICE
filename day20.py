import pandas as pd
import numpy as np

df=pd.read_csv("sc_cust_info_txn_v1.5.csv")
cust=df[["cust_class","sex_type","age","efct_svc_count","dt_stop_yn","npay_yn","r3m_avg_bill_amt","r3m_A_avg_arpu_amt","r3m_B_avg_arpu_amt", "termination_yn"]]

cust_data=removeOutliers(cust, 'avg_bill')
cust_data=removeOutliers(cust_data, 'A_bill')
cust_data=removeOutliers(cust_data, 'B_bill')

cust_data['by_age']=cust_data['age']//5*5
cust_data=cust_data.astype({'age': int, 'by_age':int})

cust_data['bill_rating'] = pd.qcut(cust_data["avg_bill"], 5 , labels=['low','lowmid', 'mid','midhigh','high'])
cust_data.head()

cust_data.to_csv('cust_data.csv', index=False)