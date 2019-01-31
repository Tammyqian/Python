import pandas as pd

df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

print df1['HPI']
print '--------------------'

# if df1['HPI'] >= 80 :
#     print df1['HPI'][0]

# if df1.HPI>=80:
#     print df1['HPI'][0]
print df1[df1['HPI']==75 | 85].count()
print '--------------------'
print df1[(df1['HPI']==75) | (df1['HPI']==85)]
print df1[(df1['HPI']== 75) | (df1['HPI']== 85)].count().to_dict()
print '---------------------'
print df1[df1['Int_rate']==1 | 3].count().to_dict()
print df1[(df1['Int_rate']== 1) | (df1['Int_rate']== 3)].count().to_dict()

