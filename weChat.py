# -*- coding: utf-8 -*-
import login
import sex
import city
import sign
import jinja2
from flask import render_template
from flask import Flask
app = Flask(__name__,static_url_path='')

@app.route('/')
def earth_point2():
    friends = login.Login().loginWeChat()
    sex.totalSex(friends)
    cityList = city.totalCity(friends)
    sign.totalSign(friends)
    return render_template('earth_point3.html', cityList=cityList)

# class Start(object):
#     def __init__(self):
#         friends = login.Login().loginWeChat()
#         sex.totalSex(friends)
#         cityList = city.totalCity(friends)
#         earth_point2(cityList)
#         sign.totalSign(friends)


if __name__ == '__main__':
    # Start()
    app.run(debug=True)