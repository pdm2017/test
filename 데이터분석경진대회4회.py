import pandas as pd
import numpy as np

df = pd.DataFrame(columns = ['LOT_ID', 'SLOT_ID', 'SITE', 'PARA_NAME', 'PARA_VALUE'])

rowid = 0;
lotlist = ['LOT'+str(i)  for i in range(10)]
paralist = ['PARA'+str(i)  for i in range(5)]

for lot in lotlist:
    print(lot, end = ',')
    for slot in range(1, 10):
        for site in range(1,22):
            for para in paralist:
                data = np.random.randn() * 10
                df.loc[rowid] = [lot, slot, site, para, data]
                rowid += 1
                
df2 = pd.pivot_table(df, index = ['LOT_ID', 'SLOT_ID', 'SITE'], columns = 'PARA_NAME', values = 'PARA_VALUE')
df2.reset_index(inplace = True)

# Unique 한 LOT_ID 목록을 가져온다
lotlist = df2['LOT_ID'].unique()

# 
tmpDf = pd.DataFrame(lotlist, columns = ['LOT_ID'])
tmpDf['label'] = 'FAIL'
tmpDf.head()

tmpDf.loc[2, 'label'] = 'UNKNOWN'
tmpDf.loc[3, 'label'] = 'UNKNOWN'
tmpDf.loc[4, 'label'] = 'PASS'

df3 = pd.merge(df2, tmpDf, how = 'inner', on = 'LOT_ID')
df3.head()

import matplotlib.pyplot as plt
%matplotlib inline

colors = {'FAIL':'red', 'PASS':'blue', 'UNKNOWN':'gray'}

# Parameter 별로 Scatter를 생성한다
# 단, 이때 color 지정이 필요하다. FAIL, PASS, UNKNOWN
paralist = ['PARA0', 'PARA2', 'PARA3', 'PARA4']
for para in paralist:
    df3.plot.scatter('SITE', para, c = df3['label'].apply(lambda x: colors[x]))
    
    
