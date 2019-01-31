import dask.dataframe as dd
import pandas as pd
import numpy as np
from scipy import interpolate
from matplotlib import pyplot as plt
from mongoUtil import MongoIns
m_util = MongoIns()
%matplotlib inline
def read_csv2(fj_num):
    df = pd.read_csv('/data/hzk/envelope_power_windspeed/f' + str(fj_num) + '_envelope.csv')
    wp_df = pd.read_csv('/data/hzk/curve_power_windspeed/f' + str(fj_num) + '_curve.csv')

    lower_data = df.PowerLower.get_values()
    upper_data = df.PowerUpper.get_values()
    speed_data = df.WindSpeed.get_values()
    wp_power_data = wp_df.Power.get_values()
    wp_speed_data = wp_df.WindSpeed.get_values()
    
    #不确定这样处理是否合理（原因：speed_data 不在 wp_speed_data 范围内，报错）
    if speed_data[-1] > wp_speed_data[-1]:
        wp_speed_data[-1] = speed_data[-1]
    if speed_data[0] < wp_speed_data[0]:
        wp_speed_data[0] = speed_data[0]
        
    interv = interpolate.interp1d(wp_speed_data, wp_power_data)#y=ax+1
    interv_Up = interpolate.interp1d(speed_data, upper_data)#y=ax+2
    interv_Lower = interpolate.interp1d(speed_data, lower_data)#y=ax+3
    
    wp_new = []
    lower_new = []
    for speed in speed_data:
        wp_new.append(interv(speed))
        lower_new.append(interv_Lower(speed))
            
    speed = []
    for s in speed_data:
        speed.append(s)
    speed.insert(0,0)
    speed.append(25)
    upper_new = []
    for u in upper_data:
        upper_new.append(u)
    upper_new.insert(0,0)
    upper_new.append(upper_new[-1])
    lower_new.insert(0,0)
    lower_new.append(lower_new[-1])
    wp_new.insert(0,0)
    wp_new.append(wp_new[-1])
    
#     fig, ax = plt.subplots()
#     ax.plot(speed, upper_new, label='upper')
#     ax.plot(speed, lower_new, label='lower')
#     ax.plot(speed, wp_new, label='wp')
    cond = {}
    field = 'fj_' + str(fj_num)
    cond['power_down'] = ','.join([str(item) for item in lower_new])
    cond['power_up'] = ','.join([str(item) for item in upper_new])
    cond['power'] = ','.join([str(item) for item in wp_new])
    cond['speed'] = ','.join([str(item) for item in speed])
#     print(speed[0],type(speed[0]))
#     m_util.m_update('wt',{'num':field},dbname='wf_HuaRui',host='192.168.111.10:27037',**cond)
    print(cond)

if __name__ == '__main__':
    read_csv2(150)


