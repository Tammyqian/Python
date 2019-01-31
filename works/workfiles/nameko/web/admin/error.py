#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bson import ObjectId
from kpages import url
from mongo_util import MongoIns
from logic.utility import BaseHandler, RpcHandler

@url(r"/admin/error")
class AdminError(RpcHandler):
	"""运维管理.无效数据"""
	def get(self):
		# 项目代号
		code_name = self.get_argument('code_name')
		# 传感类型
		sensor_type = self.get_argument('sensor_type')
		data, _ = MongoIns().m_list('data_error', dbname='error_' + code_name, sensor_type=sensor_type, sorts=[('_id', -1)], findall=True)
		
		self.write(dict(data=data))