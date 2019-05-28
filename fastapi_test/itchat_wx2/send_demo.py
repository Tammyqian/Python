import itchat, time

def lc():
    print('Finish Login!')
def ec():
    print('exit')

itchat.auto_login(loginCallback=lc, exitCallback=ec)
time.sleep()
itchat.logout()

fileDir = ''
def sendMsg():
    itchat.send_file(fileDir, toUserName=None)
    itchat.send_msg('hello world.')
    itchat.send_image(fileDir, toUserName=None)
    itchat.send_video(fileDir, toUserName=None)
itchat.auto_login()
itchat.send('hello world!')
# itchat.send('@fil@%s' % '/tmp')