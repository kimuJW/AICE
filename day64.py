import datetime
from dateutil.parser import parse
from tqdm import tqdm
from sklearn.preprocessing import MinMaxScaler

weekday_list=[]
hour_list=[]
day_list=[]

for w in tqdm(df_total['TIME_DEPARTUREDATE']):
    parse_data_w=parse(w)
    weekday_list.append(parse_data_w.weekday())
    hour_list.append(parse_data_w.hour)
    day_list.append(parse_data_w.day)
    
df_total['WEEKDAY'] = weekday_list
df_total['HOUR'] = hour_list
df_total['DAY'] = day_list

data_day=df_total['DAY']

train_data=df_total.drop(['RID','TIME_DEPARTUREDATE','TIME_ARRIVEDATE','ET','ETAA','PerHour','DAY'],axis=1)
columnNames=train_data.columns
train_data

scaler = MinMaxScaler(feature_range=(0, 1))
feature = pd.DataFrame(scaler.fit_transform(train_data))
feature.columns=columnNames
feature

feature['DAY']=data_day
train_feature=feature[feature['DAY']<=24]
train_feature=train_feature.drop(['DAY'],axis=1)
eval_feature=feature[feature['DAY']>=27]
eval_feature=eval_feature.drop(['DAY'],axis=1)

len(feature),len(train_feature),len(eval_feature)

train_target = df_total[df_total['DAY']<=24]['ET']
train_target

train_feature.to_csv('onenavi_train_feature.csv',index = False,sep='|')
train_target.to_csv('onenavi_train_target.csv',index = False,sep='|')
eval_feature.to_csv('onenavi_eval_feature.csv',index = False,sep='|')