# pandas import
import pandas as pd
import numpy as np
# !pip install Ipython
from IPython.display import Image
import matplotlib.pyplot as plt 

cust['r3m_avg_bill_amt2'] = cust['r3m_avg_bill_amt'] * 2
cust.head()

cust['r3m_avg_bill_amt3'] = cust['r3m_avg_bill_amt2'] + cust['r3m_avg_bill_amt']
cust.head()

cust.insert(10, 'r3m_avg_bill_amt10', cust['r3m_avg_bill_amt'] *10)  # 0부터 시작하여 10번째 col에 insert
cust.head()
cust.drop('r3m_avg_bill_amt10', axis=1)

cust1=cust.drop('r3m_avg_bill_amt10', axis=1)
cust1.head()

cust.drop('r3m_avg_bill_amt10', axis=1, inplace=True)