# -*- coding:utf-8 -*-

# 数据特定key
COLUMN_FIXED = ['_id', 'code_name', 'gateway_id', 'sensor_type', 'node_id', 'channel', 'dtime', 'statistic']
data = {
"gateway_id" : "bjccits1002",
"packet_name" : "BJCC-ITS",
"node_id" : "bjccits1002",
"unix_time" : "1546056260",
"LaneID" : "1",
"LaneIDFlyOver" : "1",
"Speed" : 43.00,
"Plate" : "蓝川EE9672",
"VehType" : "22",
"GrossLoad" : 1460.00,
"error" : "0",
"AL" : "0",
"GV" : "0",
"OS" : "0",
"AxleLoad1" : 730.00,
"AxleLoad2" : 730.00,
"AxleLoad3" : 0.00,
"AxleLoad4" : 0.00,
"AxleLoad5" : 0.00,
"AxleLoad6" : 0.00,
"AxleLoad7" : 0.00,
"AxleLoad8" : 0.00,
"AxleSpacing1" : 2750.00,
"AxleSpacing2" : 0.00,
"AxleSpacing3" : 0.00,
"AxleSpacing4" : 0.00,
"AxleSpacing5" : 0.00,
"AxleSpacing6" : 0.00,
"AxleSpacing7" : 0.00
}

def restore_series_data(data):
    ts = data.get('unix_time')
    data_key = 'ts'

    split_data = []
    for no, _ts in enumerate(ts):
        d = {}
        for k, v in data.items():
            if k in COLUMN_FIXED: d[k] = v
            elif k.endswith('_ts'):
                continue
            elif len(v) == len(ts):
                d[k] = v[no]
            else:
                k_ts = data.get(k + '_ts')
                if not k_ts:
                    if len(v) < len(ts): v = [v[0]] * len(ts)
                    d[k] = v[no]
                else:
                    k_ts = k_ts[0: no + 1]
                    i0 = sum([item[1] for item in k_ts[0:no]])
                    i1 = sum([item[1] for item in k_ts])
                    d[k] = v[i0: i1]

        split_data.append(d)

    return split_data
print restore_series_data(data)
