import pandas as pd
import numpy as np

df=pd.read_csv("sc_cust_info_txn_v1.5.csv")
cust=df[["cust_class","sex_type","age","efct_svc_count","dt_stop_yn","npay_yn","r3m_avg_bill_amt","r3m_A_avg_arpu_amt","r3m_B_avg_arpu_amt", "termination_yn"]]

cust=cust_fix.copy()
cust.head()
cust[['service','avg_bill','A_bill','B_bill']]=cust[['service','avg_bill','A_bill','B_bill']].fillna(0)
cust.head()
cust=cust.dropna()

print(cust['sex'].value_counts())
print(cust['class'].value_counts())
print(cust['npay'].value_counts())

cust_data=cust[(cust['class']!='H')]
print(cust_data['class'].value_counts())

cust_data=cust.copy()
cust_data['class']=cust_data['class'].replace('H','F')
print(cust_data['class'].value_counts())

cust.describe()

def removeOutliers(x, column):
    # Q1, Q3구하기
    q1 = x[column].quantile(0.25)
    q3 = x[column].quantile(0.75)
    
    # 1.5 * IQR(Q3 - Q1)
    iqr = 1.5 * (q3 - q1)
    
    # 이상치를 제거
    y=x[(x[column] < (q3 + iqr)) & (x[column] > (q1 - iqr))]
    
    return(y)

cust_data=removeOutliers(cust, 'avg_bill')
cust_data.describe()

cust_data.info()

cust_data=removeOutliers(cust_data, 'A_bill')
cust_data=removeOutliers(cust_data, 'B_bill')
cust_data.describe()

cust_data.info()

def changeOutliers(data, column):
    x=data.copy()
    # Q1, Q3구하기
    q1 = x[column].quantile(0.25)
    q3 = x[column].quantile(0.75)
    
    # 1.5 * IQR(Q3 - Q1)
    iqr = 1.5 * (q3 - q1)
    
    #이상치 대체값 설정하기
    Min = 0
    if (q1 - iqr) > 0 : Min=(q1 - iqr)
        
    Max = q3 + iqr
    
    # 이상치를 변경
    # X의 값을 직졉 변경해도 되지만 Pyhon Warning이 나오기 떄문에 인덱스를 이용
    x.loc[(x[column] > Max), column]= Max
    x.loc[(x[column] < Min), column]= Min
    
    return(x)

cust_data=changeOutliers(cust, 'avg_bill')
cust_data.describe()

cust.describe()

cust_data=changeOutliers(cust_data, 'A_bill')
cust_data=changeOutliers(cust_data, 'B_bill')
cust_data.describe()

cust_data.info()