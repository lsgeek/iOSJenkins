#coding=utf-8
import time
import urllib2
import time
import json
import mimetypes
import os
import smtplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
import json

#发送邮件
#def send_Email(json_result):
#appName = json_result['data']['appName']
#appKey = json_result['data']['appKey']
#appVersion = json_result['data']['appVersion']
#appBuildVersion = json_result['data']['appBuildVersion']
#appShortcutUrl = json_result['data']['appShortcutUrl']
#邮件接受者
mail_receivers = ['447896780@qq.com', '848949609@qq.com', '510146445@qq.com']
#根据不同邮箱配置 host，user，和pwd
mail_host = 'smtp.163.com'
mail_user = 'lsgeek@163.com'
mail_pwd = 'coffee19930410'
mail_to = ','.join(mail_receivers)
msg = MIMEMultipart()

environsString = '<h3>移动端iOS安装包</h3><p>'
environsString += '<p>内网ipa包下载地址 : ' + '暂无' + '<p>'
environsString += '<p>外网在线安装 : ' + '暂无' + '' + '<p>'
#environsString += '<p>提示 : ' + '调试中，请忽略此邮件' + '' + '<p>'
#environsString += '<li><a href="itms-services://?action=download-manifest&url=https://ssl.pgyer.com/app/plist/' + str(appKey) + '">手机直接安装</a></li>'
message = environsString
body = MIMEText(message, _subtype='html', _charset='utf-8')
msg.attach(body)
msg['To'] = mail_to
msg['from'] = mail_user
msg['subject'] = 'iOSxxx版本最新打包文件'

try:
    s = smtplib.SMTP()
    s.connect(mail_host)
    s.login(mail_user, mail_pwd)

    s.sendmail(mail_user, mail_receivers, msg.as_string())
    s.close()

    print 'success'
except Exception, e:
    print e
#############################################################