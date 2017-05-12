# -*- coding: utf-8 -*-
from echarts import Echart, Legend, Pie


def totalSex(friends):
    male = female = other = 0
    for i in friends[1:]:
        sex = i["Sex"]
        if sex == 1:
            male += 1
        elif sex == 2:
            female += 1
        else:
            other += 1
    total = len(friends[1:])
    print u"总共好友：%d" % total
    print u"男性好友：%.2f%%" % (float(male) / total * 100)
    print u"女性好友：%.2f%%" % (float(female) / total * 100)
    print u"未知性别：%.2f%%" % (float(other) / total * 100)
    chart = Echart(u'%s的微信好友性别比例' % (friends[0]['NickName']), 'from WeChat by xuqidong')
    chart.use(Pie('WeChat',
                  [{'value': male, 'name': u'男性 %.2f%%' % (float(male) / total * 100)},
                   {'value': female, 'name': u'女性 %.2f%%' % (float(female) / total * 100)},
                   {'value': other, 'name': u'未知 %.2f%%' % (float(other) / total * 100)}],
                  radius=["50%", "70%"]))
    chart.use(Legend(["male", "female", "other"]))
    del chart.json["xAxis"]
    del chart.json["yAxis"]
    chart.plot()

