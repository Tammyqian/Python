# coding:utf-8
import itchat
import time

@itchat.msg_register('Text')
def text_reply(msg):
    if not msg['FromUserName'] == myUserName:
        itchat.send_msg(u"[%s]收到好友@%s 的信息：%s\n" %
                        (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
                         msg['User']['NickName'],
                         msg['Text']), 'filehelper')
        return u'[自动回复]您好，我现在有事不在，一会再和您联系。\n已经收到您的的信息：%s\n' % (msg['Text'])


if __name__ == '__main__':
    itchat.auto_login()
    friends = itchat.get_friends(update=True)
    print(friends[1])
    myUserName = friends[0]['UserName']
    itchat.run()
