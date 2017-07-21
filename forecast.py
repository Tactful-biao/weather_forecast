# -*- coding: utf-8 -*-

'''
author : 孙士标

时间：2017-7-6

'''

import json
import requests
import datetime
import ss_rc
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(449, 686)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-image: url(:/b.png)")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 20, 191, 41))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(200, 90, 113, 41))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 160, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 160, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(110, 210, 231, 421))
        self.textEdit.setStyleSheet("background-color: rgb(217, 255, 252);")
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(120, 90, 61, 41))
        self.label_2.setStyleSheet("font: 75 10pt \"Adobe 宋体 Std L\";")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.shuchutianqi)
        self.lineEdit.returnPressed.connect(self.shuchutianqi)
        self.pushButton_2.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "天气查询"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">天气查询</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "确定"))
        self.pushButton_2.setText(_translate("Form", "退出"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\">城市：</p></body></html>"))


    def shuchutianqi(self):
        try:
            keyword = self.lineEdit.text()
            api = requests.get("http://www.sojson.com/open/api/weather/json.shtml?city=" + keyword)
            data = api.json()
            datainfo = data['data']
            forecast = datainfo['forecast']
            wendu = datainfo['wendu']
            tishi = datainfo['ganmao']
            today = datetime.date.today()
            today_high = forecast[0]['high']
            today_low = forecast[0]['low']
            tomorrow_high = forecast[1]['high']
            tomorrow_low = forecast[1]['low']
            the_day_after_tomorrow_high = forecast[2]['high']
            the_day_after_tomorrow_low = forecast[2]['low']
            tomorrow = today + datetime.timedelta(days=1)
            the_day_after_tomorrow = today + datetime.timedelta(days=2)
        except KeyError as e:
            self.textEdit.clear()
            self.textEdit.append('请输入正确的中文城市名称！')
        else:
            self.textEdit.clear()
            self.textEdit.append('城市：' + datainfo['city'])
            self.textEdit.append('今天的天气情况:')
            self.textEdit.append('时间：'+ str(today.year) + '-' + str(today.month) + '-' + str(today.day))
            self.textEdit.append('天气类型：'+ forecast[0]['type'])
            self.textEdit.append('温度：'+ today_low[3:6] + '-'+ today_high[3:6])            
            self.textEdit.append('当前温度：' + wendu)
            self.textEdit.append('最高温度：' + forecast[0]['high'])
            self.textEdit.append('最低温度：' + forecast[0]['low'])
            self.textEdit.append('风力：' + forecast[0]['fengli'])
            self.textEdit.append('风向：' + forecast[0]['fengxiang'])
            self.textEdit.append('')
            self.textEdit.append('明天的天气情况:')
            self.textEdit.append('时间：'+ str(tomorrow.year) + '-' + str(tomorrow.month) + '-' + str(tomorrow.day))
            self.textEdit.append('天气类型：' + forecast[1]['type'])
            self.textEdit.append('温度：'+ tomorrow_low[3:6] + '-' + tomorrow_high[3:6])            
            self.textEdit.append('最高温度：' + forecast[1]['high'])
            self.textEdit.append('最低温度：' + forecast[1]['low'])
            self.textEdit.append('风力：' + forecast[1]['fengli'])
            self.textEdit.append('风向：' + forecast[1]['fengxiang'])
            self.textEdit.append('')
            self.textEdit.append('后天的天气情况:')
            self.textEdit.append('时间：' + str(the_day_after_tomorrow.year) + '-' + str(the_day_after_tomorrow.month) + '-' + str(the_day_after_tomorrow.day))
            self.textEdit.append('天气类型：' + forecast[2]['type'])
            self.textEdit.append('温度：'+ the_day_after_tomorrow_low[3:6] + '-' + the_day_after_tomorrow_high[3:6])            
            self.textEdit.append('最高温度：' + forecast[2]['high'])
            self.textEdit.append('最低温度：' + forecast[2]['low'])
            self.textEdit.append('风力：' + forecast[2]['fengli'])
            self.textEdit.append('风向：' + forecast[2]['fengxiang'])
            self.textEdit.append('')
            self.textEdit.append('温馨提示：' + tishi)
            
    def clear(self):
        self.textEdit.clear()

if __name__ == '__main__':
   import sys
   app = QtWidgets.QApplication(sys.argv)
   widget = QtWidgets.QWidget()
   ui = Ui_Form()
   ui.setupUi(widget)
   widget.show()
   sys.exit(app.exec_())
