#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bson import ObjectId
from kpages import url, not_empty
from mongo_util import MongoIns
from logic.utility import BaseHandler, RpcHandler
import string
from random import choice

def add(**kwargs):
	"""
	{
		sn: 网关号
		sim: sim卡号
		pwd: 网关密码
	}
	sn 必须存在，不可为空， sim可为空
	"""
	sim = kwargs.get('sim', '')
	if sim and MongoIns().m_count('auth_gateways', sim=sim) > 0:
		return False, 'Sim卡号已经被绑定'
	sn = kwargs.get('sn')
	if MongoIns().m_count('auth_gateways', sn=sn) > 0:
		return False, '已存在相同SN'
	pwd = kwargs.get('pwd', '')
	if pwd:
		kwargs['pwd'] = pwd
	else:
		length = 8
		chars = string.ascii_letters+string.digits
		kwargs['pwd'] = ''.join([choice(chars) for i in range(length)])
	kwargs['_id'] = MongoIns().m_insert('auth_gateways', **kwargs)
	return True, kwargs


@url(r"/admin/sn")
class Sn(RpcHandler):
	"""网关管理"""
	def get(self):
		data, _ = MongoIns().m_list('auth_gateways', findall=True)
		mapUserIdName = self.rpc.idNameService.getUserIdName()
		mapProjectName = self.rpc.idNameService.getProjectName()

		# projects, _ = MongoIns().m_list('main_vsnproject', fields={'code_name': 1, 'name': 1}, findall=True)
		# mapPrjName = dict((p.get('code_name'), p.get('name')) for p in projects)

		for item in data:
			if item.get('project'):
				item['projectname'] = mapProjectName.get(item['project'], '')
			if item.get('uid'):
				item['username'] = mapUserIdName.get(item['uid'], '')
		self.write(dict(data=data, mapUserIdName=mapUserIdName))


@url(r"/admin/addsn")
class AddSNHandler(BaseHandler):
	"""
	添加网关
	{
		sn: 网关号， 不可为空
		sim: sim卡号
	}
	"""
	def post(self):
		sn = self.get_argument('sn')
		sim = self.get_argument('sim', '')
		cond = {'sn': sn, 'sim': sim}
		if sn:
			r, v = add(**cond)
			self.write(dict(status=r, msg=v))
		else:
			self.write(dict(status=False, msg='sn不存在'))
       

@url(r"/admin/delsn")
class DelSNHandler(BaseHandler):
	"""
	删除网关
	params: _id, 网关id
	"""
	def post(self):
		_id = self.get_argument('_id')
		MongoIns().m_del('auth_gateways', _id=ObjectId(_id))
		self.write(dict(status=True, msg='删除成功'))


@url(r"/admin/batchdelsn")
class BatchDelSNHandler(BaseHandler):
	"""批量删除网关"""
	def post(self):
		_ids = self.get_argument('_ids', '')
		_ids = _ids.split(',')
		_ids = [ObjectId(_id) for _id in _ids if _id]
		MongoIns().m_del('auth_gateways', _id={'$in': _ids})
		self.write(dict(status=True, msg='批量删除成功'))
	

@url(r"/admin/editsn")
class EditSNHandler(BaseHandler):
	"""编辑网关"""
	def post(self):
		sim = self.get_argument('sim', '')
		_id = self.get_argument('_id')
		if sim and MongoIns().m_count('auth_gateways', sim=sim, _id=ObjectId(_id)) > 0:
			self.write(dict(status=True, msg='编辑成功'))
		elif sim and MongoIns().m_count('auth_gateways', sim=sim) > 0:
			self.write(dict(status=False, msg='Sim卡号已经被绑定'))
		else:
			cond = {'sim': sim}
			MongoIns().m_update('auth_gateways', {'_id': ObjectId(_id)}, **cond)
			self.write(dict(status=True, msg='编辑成功'))


@url(r"/admin/getsnpwd")
class GetSNPwdHandler(BaseHandler):
	"""获取网关密码"""
	def get(self):
		_id = self.get_argument('_id')
		data = MongoIns().m_find_one('auth_gateways', _id=ObjectId(_id))
		pwd = data.get('pwd', '')
		self.write(dict(pwd=pwd))


@url(r"/admin/dissolvesn")
class DissolveSNHandler(BaseHandler):
	"""
	解绑定网关, _id, 网关id, 将用户与网关的关系解除，使字段 project='', uid='', name='',
	并且删除passport表的与该网关相关的topic
	"""
	def post(self):
		_id = self.get_argument('_id')
		sns = MongoIns().m_find_one('auth_gateways', {'_id': ObjectId(_id)})
		uid = sns.get('uid')
		sn = sns.get('sn')
		topic = 'SMB/' + sn + '/#'
		MongoIns().m_update('auth_gateways', {'_id': ObjectId(_id)}, project='', uid='', name='')
		MongoIns().m_pull('passport', {'_id': ObjectId(uid)}, host=__conf__.CAS_DB_HOST, dbname='cas', **{'topic': topic})
		self.write(dict(status=True, msg='网关解绑定成功'))


@url(r"/admin/batchdissolvesn")
class BatchDissolveSNHandler(BaseHandler):
	"""批量解绑定网关"""
	def post(self):
		_ids = self.get_argument('_ids', '')
		_ids = _ids.split(',')
		_ids = [ObjectId(_id) for _id in _ids if _id]
		users, _ = MongoIns().m_list('auth_gateways', _id={'$in': _ids})
		sns = [user['sn'] for user in users]
		uids = [ObjectId(user['uid']) for user in users]
		topics = map(lambda x: 'SMB/' + x + '/#', sns)
		MongoIns().m_update('auth_gateways', {'_id': {'$in': _ids}}, project='', uid='', name='')
		for uid in uids:
			MongoIns().m_pull('passport', {'_id': uid}, host=__conf__.CAS_DB_HOST, dbname='cas', **{'topic': {'$in': topics}})
		self.write(dict(status=True, msg='批量网关解绑定成功'))


@url(r"/admin/snuser")
class SnuserHandler(BaseHandler):
	"""
	获取网关用户
	topic列表里的元素形式是与mqtt(mosquitto)约定的
	"""
	def get(self):
		sn = self.get_argument('sn')
		topic = 'SMB/' + sn + '/#'
		data, p = MongoIns().m_list('passport', host=__conf__.CAS_DB_HOST, dbname='cas', topic=topic, findall=True)
		user = []
		for item in data:
			user.append(item.get('nickname', '') or item.get('username', ''))
		self.write(dict(user=user))


@url(r"/admin/addsnuser")
class AddSnuserHandler(BaseHandler):
	"""
	添加网关用户
	{
		sn: 网关号,
		uid: 用户id
	}
	"""
	def post(self):
		sn = self.get_argument('sn')
		uid = self.get_argument('uid', '')
		topic = 'SMB/' + sn + '/#'
		MongoIns().m_addToSet('passport', {'_id': ObjectId(uid)}, host=__conf__.CAS_DB_HOST, dbname='cas', **{'topic': topic})
		self.write(dict(status=True, msg='添加成功'))


@url(r"/admin/delsnuser")
class DelSnuserHandler(BaseHandler):
	"""删除网关用户"""
	def post(self):
		uid = self.get_argument('uid', '')
		sn = self.get_argument('sn')
		topic = 'SMB/' + sn + '/#'
		MongoIns().m_pull('passport', {'_id': ObjectId(uid)}, host=__conf__.CAS_DB_HOST, dbname='cas', **{'topic': topic})
		self.write(dict(status=True, msg='删除成功'))


@url(r"/admin/batchdelsnuser")
class BatchDelSnuserHandler(BaseHandler):
	"""批量删除网关用户"""
	def post(self):
		uid = self.get_argument('uid', '')
		sns = self.get_argument('sns', '')
		topics = map(lambda x: 'SMB/' + x + '/#', sns.split(','))
		for topic in topics:
			MongoIns().m_pull('passport', {'_id': ObjectId(uid)}, host=__conf__.CAS_DB_HOST, dbname='cas', **{'topic': topic})
		self.write(dict(status=True, msg='删除成功'))


@url(r'/admin/importsn')
class ImportSNHandler(BaseHandler):
	"""
	导入网关
	{
		sn: 网关号
		sim: sim卡号
		pwd: 网关密码
	}
	"""
	def post(self):
		f = self.request.files['hhfile'][0]
		body = f.pop('body')
		fileds = []
		exceptions = []
		data = []
		index_sn = -1

		for i, line in enumerate(body):
			# 解决换行符\r\n还是\n的问题
			if line and line[-1] == '\r':
				line = line[:-1]
		
			if i == 0:
				fileds = line.split(',')
				for f in range(len(fileds)):
					if 'sn' == fileds(f):
						index_sn = f
				if index_sn == -1:
					raise Exception('表头必须存在sn名称')
				continue
			
			if len(line) == 0: continue
			arr = line.split(',')
			# sn不可为空
			if index_sn >= len(arr) or '' == arr[index_sn]:
				arr.append("sn不可为空")
				exceptions.append(arr)
				continue
			
			val = {}
			for n, key in enumerate(fileds):
				if not key:
					continue
				if n >= len(arr):
					val[key.lower()] = ''
				else:
					val[key.lower()] = arr[n]
			
			try:
				add(**val)
				data.append(val)
			except Exception as e:
				arr.append(e.message)
				exceptions.append(arr)

		if exceptions:
			fileds.append('异常')
			exceptions.insert(0, fileds)
		
		self.write(dict(status=True, exceptions=exceptions, data=data))


@url(r"/admin/exportsn")
class ExportSNHandler(BaseHandler):
	"""
	导出网关
	导出字段为： sn, sim, pwd
	"""
	def get(self):
		cond = {'findall': True}
		sns, p = MongoIns().m_list('auth_gateways', **cond)
		fields = ['sn', 'pwd', 'sim']
		
		self.set_header("Content-Type", "text/csv")
		self.set_header('Cache-Control', 'public, max-age=4320000000')
		self.set_header('Content-disposition', 'filename=' + "SN_data.csv")

		self.write(','.join(fields).decode('utf-8').encode('GB2312'))
		self.write('\r\n')
		for item in sns:
			values = [sns.get(f,'') for f in fields]
			self.write(','.join(values).decode('utf-8').encode('GB2312'))
			self.write('\r\n')

