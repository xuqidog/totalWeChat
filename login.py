# coding:utf-8
import itchat

class Login(object):
    """docstring for ClassName"""
    def __init__(self):
        self.friends = set()

    def writeWeChat(self, data):
        fileName = u'%s的微信数据.txt' % (data[0]['NickName'])
        with open(fileName, 'w') as fp:
            fp.write('%s' % data)

    def loginWeChat(self=None):
        itchat.login()
        self.friends = itchat.get_friends(update=True)[0:]
        Login().writeWeChat(self.friends)
        return self.friends


