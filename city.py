# -*- coding: utf-8 -*-
from echarts import Echart, Legend, Series, Axis, Bar
from collections import Counter
import jieba.analyse
import requests


def totalCity(friends):
    fileName = 'totalCity.txt'
    with open(fileName, 'w') as fp:
        for i in friends:
            City = i["Province"].encode('utf8')
            # City = i["City"].encode('utf8')
            if len(City) != 0:
                fp.write('%s \n' % City)

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
    # chart = Echart(u'%s的微信好友省份分布统计' % (friends[0]['NickName']), 'from WeChat by xuqidong')
    # chart.use(Bar('China', valueList))
    # chart.use(Legend(['GDP']))
    # chart.use(Axis('category', 'left', data=nameList))
    # chart.plot()

    # {name: '海门', value: 9},
    dataList = []

    i = 0
    for name in nameList:
        value = valueList[i]
        name = name
        i += 1
        if check_contain_chinese(name.encode('utf-8')):
            GPS = geocodeG(name)
            if GPS:
                dataList.append({'name': name, 'count': value, 'address': GPS})
    return dataList

def check_contain_chinese(check_str):
      for ch in check_str.decode('utf-8'):
          if u'\u4e00' <= ch <= u'\u9fff':
             return True
      return False

#使用高德API,
def geocodeG(address):
    par = {'address': address, 'key': 'cb649a25c1f81c1451adbeca73623251'}
    base = 'http://restapi.amap.com/v3/geocode/geo'
    response = requests.get(base, par)
    answer = response.json()
    if len(answer['geocodes'])!=0:
        GPS=answer['geocodes'][0]['location'].split(",")
        print address,[float(GPS[0]),float(GPS[1])]
        return [float(GPS[0]),float(GPS[1])]