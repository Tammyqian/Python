# encoding: utf-8
import time,json
import paho.mqtt.client as mqtt

HOST = "m3.smartbow.cn"
PORT = 8885
data = {
"gateway_id" : "bjccits1002",
"packet_name" : "BJCC-ITS",
"node_id" : "bjccits1002",
"unix_time" : "1544246677",
"LaneID" : "1",
"LaneIDFlyOver" : "1",
"Speed" : 30.00,
"Plate" : "黄川E44963",
"VehType" : "24",
"GrossLoad" : 7080.00,
"error" : "0",
"AL" : "0",
"GV" : "0",
"OS" : "0",
"AxleLoad1" : 2360.00,
"AxleLoad2" : 4720.00,
"AxleLoad3" : 0.00,
"AxleLoad4" : 0.00,
"AxleLoad5" : 0.00,
"AxleLoad6" : 0.00,
"AxleLoad7" : 0.00,
"AxleLoad8" : 0.00,
"AxleSpacing1" : 5046.00,
"AxleSpacing2" : 0.00,
"AxleSpacing3" : 0.00,
"AxleSpacing4" : 0.00,
"AxleSpacing5" : 0.00,
"AxleSpacing6" : 0.00,
"AxleSpacing7" : 0.00
}
import base64
with open('/home/hcq/下载/aa.jpg','rb') as f:
    res = base64.b64encode(f.read())
client = mqtt.Client()
def on_message(mqttc, obj, msg):
    print msg.payload


def on_connect(client, userdata, flags, rc):
    print 'on connected'
    for i in range(5):
        data['unix_time'] = time.time()
        infot = client.publish('SMB/bjccits1002/1', payload=res, qos=0)
        print infot
        time.sleep(1)
        print i,data['unix_time'],infot



def test():
    client.username_pw_set('sensorcmd', '5seyQe5DfYs9Y')
    client.tls_set('ca.crt')
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(HOST, PORT, 60)   
    client.loop_forever()

if __name__ == '__main__':
    test()
