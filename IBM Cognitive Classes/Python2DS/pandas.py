import pandas as pd

df=pd.DataFrame({'a':[11,21,31],'b':[21,22,23]})
df._ix([0,0])
dir(df)
df.iloc[0,1]

