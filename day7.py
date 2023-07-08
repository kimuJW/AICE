# pandas import
import pandas as pd
import numpy as np
# !pip install Ipython
from IPython.display import Image
import matplotlib.pyplot as plt 

cust = pd.read_csv('./sc_cust_info_txn_v1.5.csv', encoding = "cp949")
cp=np.arange(10,20)
cust.index = np.arange(100, 10030)
cust.tail()
cust.loc[[289]]
cust.loc[[102, 202, 302]]
cust.iloc[[2, 102, 202]]
cust.loc[[100, 200, 300], ['cust_class', 'sex_type', 'age', 'r3m_avg_bill_amt', 'r3m_A_avg_arpu_amt']]
cust.iloc[[0, 100, 200], [3, 4, 5, 9, 10]]
cust.loc[[100, 200, 300], [3, 4, 5, 9, 10]]

extract = cust[(cust['sex_type']=='M') & (cust['r3m_avg_bill_amt']>=50000) & (cust['r3m_avg_bill_amt']< 100000)]
extract.head()

sex = cust['sex_type']=='M'
bill = (cust['r3m_avg_bill_amt']>=50000) & (cust['r3m_avg_bill_amt']< 100000)
cust[sex & bill].head()