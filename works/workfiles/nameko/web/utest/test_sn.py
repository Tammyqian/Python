# -*- coding:utf-8 -*-
"""
    author leicj@smartbow.net
"""
import json
from unittest import TestCase
from admin.sn import add, MongoIns, ObjectId

class SnCase(TestCase):
	def test_add(self):
		# test1, 添加网关，删除网关, 编辑网关
		kwargs = {'sn': '11111', 'sim': '33333'}
		r, v = add(**kwargs)
		if not r:
			print r, v
			raise "添加网关失败!"
		MongoIns().m_del('auth_gateways', _id=ObjectId(v['_id']))
		# test2
		r, v = add(**kwargs)
		kwargs1 = {'sn': '11111'}
		r1, v1 = add(**kwargs1)
		if r1:
			MongoIns().m_del('auth_gateways', _id=ObjectId(v1['_id']))
			print r1, v1
			raise "网关号应该保持唯一"
		MongoIns().m_del('auth_gateways', _id=ObjectId(v['_id']))
		#test3
		r, v = add(**kwargs)
		print r, v
		sim = '44444'
		if sim and MongoIns().m_count('auth_gateways', sim=sim, _id=ObjectId(v['_id'])) > 0:
			print True, '未做修改，编辑成功'
		elif sim and MongoIns().m_count('auth_gateways', sim=sim) > 0:
			print False, 'Sim卡号已经被绑定'
		else:
			kwargs['sim'] = sim
			MongoIns().m_update('auth_gateways', {'_id': ObjectId(v['_id'])}, **kwargs)
			print True, '编辑成功'
		MongoIns().m_del('auth_gateways', _id=ObjectId(v['_id']))

	def test_addsnuser(self):
		#test4, 增加网关用户, 删除网关用户
		kwargs = {'sn': '11111', 'uid': '5b0bce3d17cfb00006d37799'}
		sn = kwargs['sn']
		topic = 'SMB/' + sn + '/#'
		MongoIns().m_addToSet('passport', {'_id': ObjectId(kwargs['uid'])}, host=__conf__.CAS_DB_HOST, dbname='cas', **{'topic': topic})
		print True, '添加成功'
		MongoIns().m_pull('passport', {'_id': ObjectId(kwargs['uid'])}, host=__conf__.CAS_DB_HOST, dbname='cas', **{'topic': topic})
		print True, '删除成功'

	# def test_dissolvesn(self):
	# 	#test6, 解绑定网关
	# 	kwargs = {'_id': "5c4ecb2bbde60b388eb2f44f"}
	# 	sns = MongoIns().m_find_one('auth_gateways', _id=ObjectId(kwargs['_id']))
	# 	sn = sns.get('sn')
	# 	uid = sns.get('uid','')
	# 	MongoIns().m_update('auth_gateways', {'_id': ObjectId(kwargs['_id'])}, project='', uid='', name='')
	# 	topic = 'SMB/' + sn + '/#'
	# 	MongoIns().m_pull('passport', {'_id': ObjectId(uid)}, host=__conf__.CAS_DB_HOST, dbname='cas', **{'topic': topic})
	# 	print True, '网关解绑定成功'
		
		