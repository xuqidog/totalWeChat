# -*- coding: utf-8 -*-
from echarts import Echart, Legend, Series, Axis, Bar
from collections import Counter
import jieba.analyse


def totalCity(friends):
    fileName = 'totalCity.txt'
    with open(fileName, 'w') as fp:
        for i in friends:
            Province = i["Province"].encode('utf8')
            # City = i["City"].encode('utf8')
            if len(Province) != 0:
                fp.write('%s \n' % Province)

    # 统计
    bill_path = r'totalCity.txt'
    bill_result_path = r'cityCount.txt'
    with open(bill_path, 'r') as fr:
        data = jieba.cut(fr.read())
    data = dict(Counter(data))
    valueList = []
    nameList = []
    with open(bill_result_path, 'w') as fw:
        for k, v in data.items():
            if len(k) >= 2:
                valueList.append(v)
                nameList.append(k)
                fw.write("%s,%d\n" % (k.encode('utf-8'), v))

    # 用echart画图
    chart = Echart(u'%s的微信好友省份分布统计' % (friends[0]['NickName']), 'from WeChat by xuqidong')
    chart.use(Bar('China', valueList))
    chart.use(Legend(['GDP']))
    chart.use(Axis('category', 'left', data=nameList))
    chart.plot()
