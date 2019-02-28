# -*- coding:utf-8 -*-

from nameko.dependency_providers import Config
from nameko.rpc import rpc
from mongo import MongoIns
from bson import ObjectId

class IdNameService:
	name = "idNameService"
	# 配置文件
	config = Config()

	@property
	def host(self):
		return self.config['MONGO_CONFIG']['sensorcmd']['DB_HOST']
	@property
	def dbname(self):
	    return self.config['MONGO_CONFIG']['sensorcmd']['DB_NAME']
	# @property
	# def cashost(self):
	# 	return self.config['MONGO_CONFIG']['sensorcmd']['CAS_DB_HOST']
    
	@rpc
	def getUserIdName(self):
		users, _ = MongoIns().m_list('passport', host='192.168.111.149:27017', dbname='cas', fields={'nickname': 1, 'username': 1}, findall=True)
		mapUserIdName = dict((u.get('_id'), u.get('nickname', '') or u.get('username', '')) for u in users)
		return mapUserIdName

	@rpc
	def getProjectName(self):
		projects, _ = MongoIns().m_list('main_vsnproject', host=self.host, dbname=self.dbname, fields={'code_name': 1, 'name': 1}, findall=True)
		mapProjectName = dict((p.get('code_name', ''), p.get('name', '')) for p in projects)
		return mapProjectName
