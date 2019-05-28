# coding:utf-8
import itchat
import re
from itchat.content import *

# itchat.login()
# itchat.send('Hello, filehelper', toUserName='@897741a7fc70687a4a6fa8e017c922b698967685ff4a40f06d550471cf3fa69a')


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    print(msg)
    print(msg.text)
    # return msg.text

add_friend_compile = re.compile(r'Python|Py|加群')
@itchat.msg_register(itchat.content.FRIENDS)
def deal_with_friend(msg):
    if add_friend_compile.search(msg['Content']) is not None:
        itchat.add_friend(**msg['Text'])
        itchat.send_msg('nice to meet you', msg['RecommendInfo']['UserName'])
        itchat.send_image('welcome.png', msg['RecommendInfo']['UserName'])

# 获得群聊id
def get_group_id(group_name):
    group_list = itchat.search_chatrooms(name=group_name)
    return group_list[0]['UserName']

"""
自动处理信息
１．加好友后发送加群信息
２．过滤加群信息
３．公众号推荐
４．打赏
"""
@itchat.msg_register([TEXT])
def deal_with_msg(msg):
    text = msg['Content']
    if text == u'加群':
        itchat.add_member_into_chatroom(get_group_id('小猪的Python学习交流群'),
                                        [{'UserName':msg['FromUserName']}], useInvitation=True)
    elif text == u'博客':
        return 'coder-pig的个人主页-掘金 :https://juejin.im/user/570afb741ea493005de84da3'
    elif text == u'公众号':
        itchat.send_image('gzh.jpg', msg['FromUserName'])
    elif text == u'打赏':
        itchat.send_image('ds.gif', msg['FromUserName'])
        itchat.send_msg('Thank you', msg['FromUserName'])
        itchat.send_image('wxpay.png', msg['FromUserName'])
    else:
        itchat.send_image('hrwh.png', msg['FromUserName'])

itchat.auto_login()
itchat.run()
