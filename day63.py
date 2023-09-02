!pip install tqdm

import datetime
from dateutil.parser import parse
from tqdm import tqdm

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

new_df_eval=df_total[df_total['DAY']>=27]
new_df_eval.to_csv("onenavi_evaluation_new.csv",sep="|",index=False)

dummy_fields = ['WEEKDAY','HOUR','level1_pnu','level2_pnu']

for dummy in dummy_fields:
    dummies = pd.get_dummies(df_total[dummy], prefix=dummy, drop_first=False)
    df_total = pd.concat([df_total, dummies], axis=1)
    
df_total = df_total.drop(dummy_fields,axis=1)