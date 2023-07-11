import numpy as np
import pandas as pd

data = pd.DataFrame({'cust_id': ['cust_1', 'cust_1', 'cust_1', 'cust_2', 'cust_2', 'cust_2', 'cust_3', 'cust_3', 'cust_3'],
                  'prod_cd': ['p1', 'p2', 'p3', 'p1', 'p2', 'p3', 'p1', 'p2', 'p3'],
                  'grade' : ['A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B'],
                  'pch_amt': [30, 10, 0, 40, 15, 30, 0, 0, 10]})

data.pivot(index = 'cust_id', columns ='prod_cd', values ='pch_amt')
data.pivot('cust_id', 'prod_cd', 'pch_amt')

data.pivot_table(index = 'cust_id', columns ='prod_cd', values ='pch_amt')
data.pivot(index = ['cust_id','grade'], columns ='prod_cd', values ='pch_amt')
data.pivot_table(index = ['cust_id','grade'], columns ='prod_cd', values ='pch_amt')
data.pivot(index = 'cust_id', columns =['grade','prod_cd'], values ='pch_amt')
data.pivot_table(index = 'cust_id', columns =['grade','prod_cd'], values ='pch_amt')
data.pivot(index='grade', columns='prod_cd', values='pch_amt')  
data.pivot_table(index='grade', columns='prod_cd', values='pch_amt')  

data.pivot_table(index='grade', columns='prod_cd', values='pch_amt', aggfunc=np.sum)
pd.pivot_table(data, index='grade', columns='prod_cd', values='pch_amt', aggfunc=np.sum)
data.pivot_table(index='grade', columns='prod_cd', values='pch_amt', aggfunc=np.mean)