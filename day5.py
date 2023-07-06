import pandas as pd
import numpy as np
# !pip install Ipython
from IPython.display import Image

cust = pd.read_csv('./sc_cust_info_txn_v1.5.csv', encoding = "cp949")

cust.head(n=3)
cust.tail(n=10)
cust.shape
cust.columns
cust.info()
cust.describe()
cust.dtypes

cust2 = pd.read_csv('./sc_cust_info_txn_v1.5.csv', index_col='cust_class', usecols=['cust_class', 'r3m_avg_bill_amt', 'r3m_B_avg_arpu_amt', 'r6m_B_avg_arpu_amt'])
cust2