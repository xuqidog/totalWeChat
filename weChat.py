# -*- coding: utf-8 -*-
import login
import sex
import city
import sign

class Start(object):
    def __init__(self):
        friends = login.Login().loginWeChat()
        sex.totalSex(friends)
        city.totalCity(friends)
        sign.totalSign(friends)


if __name__ == '__main__':
    Start()
