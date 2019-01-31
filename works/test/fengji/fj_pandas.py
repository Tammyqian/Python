import dask.dataframe as dd
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
%matplotlib inline

def read_csv(fj_num):
    df = pd.read_csv('/data/hzk/envelope_power_windspeed/f'+str(fj_num)+'_envelope.csv')
    lower_data = df.PowerLower.get_values()
    lower_last = lower_data[-1]
    upper_data = df.PowerUpper.get_values()
    upper_last = upper_data[-1]
    speed_data = df.WindSpeed.get_values()
    speed_last = speed_data[-1]
    speed = [0,speed_last,25]
    lower = [0,lower_last,lower_last]
    upper = [0,upper_last,upper_last]
    fj_data = [lower,upper,speed]
    return fj_data

def read_csv2(fj_num):
    df = pd.read_csv('/data/hzk/envelope_power_windspeed/f' + str(fj_num) + '_envelope.csv')
    wp_df = pd.read_csv('/data/hzk/curve_power_windspeed/f' + str(fj_num) + '_curve.csv')

    lower_data = df.PowerLower.get_values()
    upper_data = df.PowerUpper.get_values()
    speed_data = df.WindSpeed.get_values()
    wp_power_data = wp_df.Power.get_values()
    wp_speed_data = wp_df.WindSpeed.get_values()
    lower = []
    upper = []
    speed = []
    wp_power = []
    wp_speed = []
    for l in lower_data:
        lower.append(l)
    for u in upper_data:
        upper.append(u)
    for s in speed_data:
        speed.append(s)
    for wp in wp_power_data:
        wp_power.append(wp)
    for ws in wp_speed_data:
        wp_speed.append(ws)

    lower.insert(0,0)
    upper.insert(0,0)
    speed.insert(0,0)
    lower.append(lower[-1])
    upper.append(upper[-1])
    speed.append(25)

    fj_data = [lower, upper, speed]
    # return fj_data
    
    if speed_data[-1] > wp_speed_data[-1]:
        wp_speed_data[-1] = speed_data[-1]
    if speed_data[0] < wp_speed_data[0]:
        wp_speed_data[0] = speed_data[0]

    interv = interpolate.interp1d(wp_speed_data, wp_power_data)
    interv_Up = interpolate.interp1d(speed_data, upper_data)
    interv_Lower = interpolate.interp1d(speed_data, lower_data)

    wp_new = []
    lower_new = []
    for speed in speed_data:
        wp_new.append(interv(speed))
        lower_new.append(interv_Lower(speed))

if __name__ == '__main__':
    for num in range(133,167):
        read_csv(num)
