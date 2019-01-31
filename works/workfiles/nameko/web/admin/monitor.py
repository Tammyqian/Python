from bson import ObjectId
from kpages import url, not_empty, get_members
from mongo_util import MongoIns
from logic.utility import BaseHandler, RpcHandler

@url(r"/admin/monitor")
class MonitorHandler(BaseHandler):
	"""传感模块"""
	def get(self):
		monitors, _ = MongoIns().m_list('monitor', findall=True, data_type=0)
		models, _ = MongoIns().m_list('aimodel', findall=True)
		product_versions, _ = MongoIns().m_list('product_version', findall=True)

		member_filter = lambda m: isinstance(m, type) and hasattr(m, '__dataview__')
		plugin_members = get_members('plat', member_filter)
		plugin_members_name = {k: v.__doc__ for k, v in plugin_members.items()}

		product_map = dict((item.get('_id'), item.get('product_type', '')) for item in product_versions)

		for m in monitors:
			if not m.get('apply_product'):
				m['apply_product'] = []
				continue
			m['apply_product'] = ','.join([product_map[item] for item in m['apply_product']])
		
		self.write(dict(monitors=monitors))


