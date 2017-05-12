# coding:utf-8
import re
from pylab import *
from wordcloud import WordCloud
import jieba


def totalSign(friends):
    tList = []
    fileName = u'%s的微信好友所有签名.txt' % (friends[0]['NickName'])
    with open(fileName, 'w') as fp:
        for i in friends:  # 获取个性签名
            signature = i["Signature"].strip().replace("span", "").replace("class", "").replace("emoji",
                                                                                                "")  # 正则匹配过滤掉emoji表情，例如emoji1f3c3等
            rep = re.compile("1f\d.+")
            signature = rep.sub("", signature)
            tList.append(signature)
            fp.write('%s \n' % signature.encode('utf8'))

    # 拼接字符串
    text = "".join(tList)
    # jieba分词import jieba
    wordlist_after_jieba = jieba.cut(text, cut_all=True)
    wl_space_split = " ".join(wordlist_after_jieba)
    backgroud_Image = plt.imread('timg.jpeg')
    my_wordcloud = WordCloud(font_path='/Users/xuqidong/totalWeChat/SimHei.ttf', background_color='white',
                             mask=backgroud_Image, )
    my_wordcloud.generate(wl_space_split)
    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.show()
