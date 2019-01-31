# -*- coding:utf-8 -*-
#!/usr/bin/python

import time
import uuid
import json
import logging
import paho.mqtt.client as mqtt
from setting import *

from log import log
level = logging.DEBUG if DEBUG else logging.INFO
_log = log(LOG_FILE + '_mq', level = level).getLogger()


oclient = None 
class MQTTClass:
    def __init__(self, clientid=None, host='localhost', port=1883, topic="$SYS/#" ,qos=0):
        self._host = host
        self._port = port
        self._topic = topic
        self._qos = qos or QOS

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
        self._mqttc.subscribe(topic, qos or QOS)

    def mqtt_pub(self,topic,msg):
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

class M3(MQTTClass):
    def mqtt_on_connect(self, mqttc, obj, flags, rc):
        if rc:
            print rc,'m3 not connected'
        else:
            print rc,'m3 connected'
        topic = TOPIC or '$SYS/#'
        self.mqtt_sub(topic, qos=QOS or 0)

    def mqtt_on_message(self, mqttc, obj, msg):
        data = json.loads(msg.payload)
        topic = 'SR/up/data/'+ data['gateway_id'] 
        _log.info(topic)
        _log.info(data)
        print data
        oclient.mqtt_pub(topic, json.dumps(data))


class M1(MQTTClass):
    def mqtt_on_connect(self, mqttc, obj, flags, rc):
        if rc:
            print('m1 not connected',rc)
        else:
            print('m1 connected',rc)
            



if __name__ == '__main__':
    _mqtt = M3(clientid = str(uuid.uuid1()), host = M3_HOST, port = M3_PORT)
    _mqtt.mqtt_tls_set(M3_CERTS)
    _mqtt.username_pw_set(M3_USER, M3_PWD)
    _mqtt.mqtt_connect()


    oclient = M1(clientid='m1', host=M1_HOST, port=M1_PORT)
    oclient.mqtt_tls_set(CA_CERTS, CERTFILE, KEYFILE)
    oclient.mqtt_connect()
    while True:
        oclient.mqtt_loop()
        _mqtt.mqtt_loop()
