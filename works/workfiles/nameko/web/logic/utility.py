# -*- coding:utf-8 -*-
from tornado.web import RequestHandler
from tornado.websocket import WebSocketHandler
from nameko.standalone.rpc import ClusterRpcProxy
from kpages import ContextHandler
from tornado.web import RequestHandler

CONFIG = dict(AMQP_URI=__conf__.AMQP_URI)
class RPCContextHandler(object):
	"""
	base handler for session
	"""
	def _execute(self, transforms, *args, **kwargs):
		''' select base handler for self '''
		with ClusterRpcProxy(CONFIG) as rpc:
			self.rpc = rpc
			if isinstance(self, WebSocketHandler):
				WebSocketHandler._execute(self, transforms, *args, **kwargs)
			elif isinstance(self, RequestHandler):
				RequestHandler._execute(self, transforms, *args, **kwargs)

__all__ = ["RPCContextHandler"]

class BaseHandler(ContextHandler,RequestHandler):
	def set_default_headers(self):
		self.set_header("Access-Control-Allow-Origin", "*")
		self.set_header("Access-Control-Allow-Headers", "x-requested-with")
		self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

	def options(self, *args, **kwargs):
		self.set_header("Access-Control-Allow-Origin", "*")
		self.set_header("Access-Control-Allow-Headers", "x-requested-with")
		self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

class RpcHandler(RPCContextHandler, BaseHandler):
	pass