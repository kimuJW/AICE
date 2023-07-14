import pandas as pd
import numpy as np
from IPython.display import Image

customer = pd.DataFrame({'cust_id' : np.arange(6), 
                    'name' : ['철수', '영희', '길동', '영수', '수민', '동건'], 
                    '나이' : [40, 20, 21, 30, 31, 18]})

orders = pd.DataFrame({'cust_id' : [1, 1, 2, 2, 2, 3, 3, 1, 4, 9], 
                    'item' : ['치약', '칫솔', '이어폰', '헤드셋', '수건', '생수', '수건', '치약', '생수', '케이스'], 
                    'quantity' : [1, 2, 1, 1, 3, 2, 2, 3, 2, 1]})


pd.merge(customer, orders, on='cust_id')  
pd.merge(customer, orders, on='cust_id', how='inner') 
pd.merge(customer, orders, on='cust_id', how='left')
pd.merge(customer, orders, on='cust_id', how='right')
pd.merge(customer, orders, on='cust_id', how='outer')

cust1 = customer.set_index('cust_id')
order1 = orders.set_index('cust_id')

pd.merge(cust1, order1, left_index=True, right_index=True)
pd.merge(customer, orders, on='cust_id', how='right').groupby('item').sum()
pd.merge(customer, orders, on='cust_id', how='right').groupby('item').sum().sort_values(by='quantity', ascending=False)

pd.merge(customer, orders, on='cust_id', how='inner').groupby(['name', 'item']).sum().loc['영희']
cust1.join(order1, how='inner')