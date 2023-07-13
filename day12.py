import pandas as pd
import numpy as np
from IPython.display import Image

df1 = pd.DataFrame({'key1' : [0,1,2,3,4], 'value1' : ['a', 'b', 'c','d','e']}, index=[0,1,2,3,4])
df2 = pd.DataFrame({'key1' : [3,4,5,6,7], 'value1' : ['c','d','e','f','g']}, index=[3,4,5,6,7])

pd.concat([df1, df2], ignore_index=False)
pd.concat([df1, df2], ignore_index=True)
pd.concat([df1, df2], axis =1)
pd.concat([df1, df2], axis =0)

df3 = pd.DataFrame({'a':['a0','a1','a2', 'a3'], 'b':['b0','b1','b2','b3'], 'c':['c0','c1','c2','c3']}, index = [0,1,2,3])
df4 = pd.DataFrame({'a':['a2','a3','a4', 'a5'], 'b':['b2','b3','b4','b5'], 'c':['c2','c3','c4','c5'], 'd':['d1','d2','d3','d4']}, index = [2,3,4,5])
pd.concat([df3, df4], join='outer')
pd.concat([df3, df4], join='inner')

df5 = pd.DataFrame({'A':['A0','A1','A2'], 'B':['B0','B1','B2'], 'C':['C0','C1','C2'], 'D':['D0','D1','D2']}, index=['I0','I1','I2'])
df6 = pd.DataFrame({'A':['AA2','A3','A4'], 'B':['BB2','B3','B4'], 'C':['CC2','C3','C4'], 'D':['DD2','D3','D4']}, index=['I2','I3','I4'])

pd.concat([df5, df6], verify_integrity=False)
pd.concat([df5, df6], verify_integrity=True)