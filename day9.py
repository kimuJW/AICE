import pandas as pd
import numpy as np
# !pip install Ipython
from IPython.display import Image

cust = pd.read_csv('./sc_cust_info_txn_v1.5.csv', encoding = "cp949")

gender_group = cust.groupby('sex_type')

gender_group.groups
gender_group.count()
gender_group.mean()
gender_group.max()
gender_group.mean()[['r3m_avg_bill_amt']]
gender_group.mean()[['r3m_avg_bill_amt']]
cust.groupby('sex_type').mean()[['r3m_avg_bill_amt']]
cust.groupby(['cust_class', 'sex_type']).mean()[['r3m_avg_bill_amt']]
multi_group=cust.groupby(['cust_class', 'sex_type'])
multi_group.mean()[['r3m_avg_bill_amt']]
cust.groupby(['cust_class', 'sex_type']).mean().loc[[("D","M")]]
cust.set_index(['cust_class','sex_type'])
cust.set_index(['cust_class','sex_type']).reset_index()
cust.set_index(['cust_class','sex_type']).groupby(level=[0]).mean()
cust.set_index(['cust_class','sex_type']).groupby(level=[0,1]).aggregate([np.mean, np.max])