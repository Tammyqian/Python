#!/bin/bash

for i in {1..2}
do
   mosquitto_pub -h m3.smartbow.cn -t SMB/bjccits1002/1 -p 8885 --cafile ca.crt -u yunwei -P 1234567809 -m '{"VehType": "24", "AxleSpacing7": 0.0, "AxleSpacing6": 0.0, "AxleSpacing5": 0.0, "AxleSpacing4": 0.0, "AxleSpacing3": 0.0, "AxleSpacing2": 0.0, "AxleSpacing1": 5046.0, "AxleLoad8": 0.0, "AxleLoad7": 0.0, "AxleLoad6": 0.0, "AxleLoad5": 0.0, "AxleLoad4": 0.0, "AxleLoad3": 0.0, "AxleLoad2": 4720.0, "AxleLoad1": 2360.0, "gateway_id": "bjccits1002", "Plate": "\\u9ec4\\u5dddE44963", "Speed": 30.0, "GV": "0", "AL": "0", "LaneID": "1", "LaneIDFlyOver": "1", "GrossLoad": 7080.0, "unix_time": "1544246677", "node_id": "bjccits1002", "error": "0", "packet_name": "BJCC-ITS", "OS": "0"}'
done
