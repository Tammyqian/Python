# -*- coding:utf-8 -*-
#!/usr/bin/python

import time
import uuid
import json
import logging
import paho.mqtt.client as mqtt
from mqttrouter.setting import *

from mqttrouter.log import log
level = logging.DEBUG if DEBUG else logging.INFO
_log = log(LOG_FILE + '_mq', level = level).getLogger()


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
        self._mqttc.publish(topic, msg,qos=1)


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
            # time.sleep(3)
            self.mqtt_connect()

        return rc



class M3(MQTTClass):
    def mqtt_on_connect(self, mqttc, obj, flags, rc):
        print 'm3 connected'
        _log.info("MQTT3 Connect successful")
        topic = 'SMB/#'
        self.mqtt_sub(topic)
        print 'sub',topic

    def mqtt_on_message(self, mqttc, obj, msg):
        data = json.loads(msg.payload)
        print data
        # topic = 'SR/up/data/'+ data['gateway_id']
        # if oclient._mqttc.loop():
        #     oclient.mqtt_connect()
		#
        # _log.info(topic)
        # _log.info(data)
        # oclient.mqtt_pub(topic, json.dumps(data))


class M1(MQTTClass):
    def mqtt_on_connect(self, mqttc, obj, flags, rc):
        print('m1 connected')
        _log.info("MQTT1 Connect successful")


import time
if __name__ == '__main__':
    oclient = M3(clientid = str(uuid.uuid1()), host = M3_HOST, port = M3_PORT)
    oclient.mqtt_tls_set(M3_CERTS)
    oclient.username_pw_set(M3_USER, M3_PWD)
    oclient.mqtt_connect()
    for i in range(50):
        data = {u'num':i,u'VehType': u'23', u'AxleSpacing7': 0.0, u'AxleSpacing6': 0.0, u'AxleSpacing5': 0.0, u'AxleSpacing4': 0.0,
         u'AxleSpacing3': 0.0, u'AxleSpacing2': 0.0, u'AxleSpacing1': 3012.0, u'AxleLoad8': 0.0, u'AxleLoad7': 0.0,
         u'AxleLoad6': 0.0, u'AxleLoad5': 0.0, u'AxleLoad4': 0.0, u'AxleLoad3': 0.0, u'AxleLoad2': 800.0,
         u'AxleLoad1': 800.0, u'gateway_id': u'bjccits1002', u'Plate': u'\u84dd\u5dddEA5785', u'Speed': 33.0,
         u'GV': u'0', u'AL': u'0', u'LaneID': u'4', u'LaneIDFlyOver': u'4', u'GrossLoad': 1600.0,
         u'unix_time': u'1545130312', u'node_id': u'bjccits1002', u'error': u'0', u'packet_name': u'BJCC-ITS',
         u'OS': u'0'}
        time.sleep(1)
        oclient.mqtt_pub("SMB/1", json.dumps(data))
