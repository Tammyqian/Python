# encoding: utf-8
#!/usr/bin/python

import time
import uuid
import json
import paho.mqtt.client as mqtt


oclient = None 
class MQTTClass:
    def __init__(self, clientid=None, host='localhost', port=1883, topic="$SYS/#", qos=0):
        self._host = host
        self._port = port
        self._topic = topic
        self._qos = qos

        self._mqttc = mqtt.Client(clientid)
        self._mqttc.on_message = self.mqtt_on_message
        self._mqttc.on_connect = self.mqtt_on_connect
        self._mqttc.on_publish = self.mqtt_on_publish
        self._mqttc.on_subscribe = self.mqtt_on_subscribe
        self._mqttc.on_disconnect = self.mqtt_on_disconnect


    def mqtt_connect(self):
        try:
            self._mqttc.connect(self._host, self._port)
        except Exception as e:
            pass

    def mqtt_sub(self, topic="$SYS/#", qos=0):
        self._mqttc.subscribe(topic, qos)

    def mqtt_pub(self, topic, msg):
        self._mqttc.publish(topic, msg)


    def mqtt_tls_set(self, ca_certs, certfile=None, keyfile=None):
        self._mqttc.tls_set(ca_certs, certfile, keyfile)

    def username_pw_set(self, username, password=None):
        self._mqttc.username_pw_set(username, password)

    def mqtt_on_connect(self, mqttc, obj, flags, rc):
        pass

    def mqtt_on_message(self, mqttc, obj, msg):
        pass 

    def mqtt_on_publish(self, mqttc, obj, mid):
        pass

    def mqtt_on_subscribe(self, mqttc, obj, mid, granted_qos):
        pass

    def mqtt_on_log(self, mqttc, obj, level, string):
        pass

    def mqtt_on_disconnect(self, mqttc, userdata, rc):
        pass

    def mqtt_loop(self):
        rc = self._mqttc.loop(timeout=3)
        if rc:
            time.sleep(3)
            self.mqtt_connect()

        return rc

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

class M1(MQTTClass):
    def mqtt_on_connect(self, mqttc, obj, flags, rc):
        print 'm1 connected'
        topic ="SR/up/data/bjccits1002" 
        print self._mqttc.loop()
        print self.mqtt_pub(topic, json.dumps(data))
        
        #self.mqtt_sub('SR/up/data/FAB411181716758')

    def mqtt_on_message(self, mqttc, obj, msg):
        print msg.topic,msg.payload


if __name__ == '__main__':

    o_host = 'm1.smartbow.cn'
    CA_CERTS = "CA_file/ca.crt"
    CERTFILE = "CA_file/client.crt"
    KEYFILE = "CA_file/client.key"

    oclient = M1(clientid='m1', host=o_host, port=1883)
    oclient.mqtt_tls_set(CA_CERTS, CERTFILE, KEYFILE)
    oclient.mqtt_connect()
    while True:
        oclient.mqtt_loop()
