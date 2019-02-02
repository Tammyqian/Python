# -*- coding:utf-8 -*-
from asyncore import dispatcher
import socket, asyncore

from asynchat import async_chat

PORT = 5005

#升级
class ChatSession(async_chat):
    def __init__(self, sock):
        async_chat.__init__(self, sock)
        self.set_terminator('\r\n')
        self.data = []

    def collect_incoming_data(self, data):
        self.data.append(data)

    def found_terminator(self):
        line = ''.join(self.data)
        self.data = []
        #处理这行数据......
        print line


class ChatServer(dispatcher):
    def __init__(self, port):
        dispatcher.__init__(self)
        # super(ChatServer,self).__init__()
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('', port))
        self.listen(5)

        self.sessions = []

    def handle_accept(self):
        coon, addr = self.accept()
        print 'Connection attempt from', addr[0]

        self.sessions.append(ChatSession(coon))

if __name__ == '__main__':
    s = ChatServer(PORT)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        print