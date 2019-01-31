import pandas as pd
import numpy as np
frame = pd.DataFrame(np.arange(9).reshape((3,3)),index=['a','c','d'],
                     columns=['Ohio','Texas','California'])
print frame
frame2 = frame.reindex(['a','b','c','d'])
print frame2

states = ['Texas', 'Utah', 'California']
frame3 = frame.reindex(columns=states)
print frame3

data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print data
print data.drop(['Colorado','Ohio'])
print data.drop('two',axis=1)
print data.drop(['two'])
