# pandas import
import pandas as pd
import numpy as np
# !pip install Ipython
from IPython.display import Image

cust = pd.read_csv('./sc_cust_info_txn_v1.5.csv', encoding = "cp949")

cust.cust_class = cust['cust_class']

cust[['cust_class']] #데이터 프레임 형태로 가져오기

cust[['cust_class', 'age', 'r3m_avg_bill_amt']] # 복수의 컬럼 선택

cust[7:10] # 데이터프레임 슬라이싱