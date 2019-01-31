# -*- coding:utf-8 -*-
import dask.dataframe as dd

df = dd.read_csv('f_key.csv')
print df
# df = df + str(100)
# df = df[df.name == 'Alice']