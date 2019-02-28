#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bson import ObjectId
from kpages import url
from mongo import MongoIns
from logic.utility import BaseHandler, RpcHandler

@url(r"/project/idname")
class ProjectIdName(BaseHandler):
	"""辅助函数.获取所有项目的id/name"""
	def get(self):
		data, _ = MongoIns().m_list('main_vsnproject', fields={'name': 1, 'code_name': 1}, findall=True)
		mapProjectIdName = dict((d.get('_id'), d.get('name')) for d in data)
		mapProjectCodeName = dict((d.get('code_name'), d.get('name')) for d in data)
		self.write(dict(mapProjectIdName=mapProjectIdName, mapProjectCodeName=mapProjectCodeName))


@url(r"/sensortype/idname")
class SensorTypeIdName(RpcHandler):
	"""辅助函数.获取传感类型的id/name"""
	def get(self):
		"""
			1. 传感类型包含两类: 通用传感类型 和 项目特有传感类型.
			2. 传感类型以code_name作为标识符. 如果项目和通用的code_name相同, 则以项目为标准.
			备注: 传感类型的code_name命名不规范, 应该叫做sensor_type.
		"""
		# 项目代号
		code_name = self.get_argument('code_name', None)
		if code_name:
			sensor_types = self.rpc.smlibToolService.get_monitors(code_name=code_name)
		else:
			sensor_types = self.rpc.smlibToolService.get_monitors()

		mapSensortypeCodeName = dict((s.get('code_name'), s.get('full_name')) for s in sensor_types)
		self.write(dict(mapSensortypeCodeName=mapSensortypeCodeName))