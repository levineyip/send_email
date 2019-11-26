#! /usr/bin/env python#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

#qq邮箱smtp服务器host_server = 'smtp.qq.com'#sender_qq为发件人的qq号码sender_qq = '7697****@qq.com'#pwd为qq邮箱的授权码pwd = '*****mkenb****' ###发件人的邮箱sender_qq_mail = '7697****@qq.com'#收件人邮箱receiver = 'yiibai.com@gmail.com'#邮件的正文内容mail_content = "你好，<p>这是使用python登录qq邮箱发送HTML格式邮件的测试：</p><p><a href='http://www.yiibai.com'>易百教程</a></p>"#邮件标题mail_title = 'Maxsu的邮件'#邮件正文内容msg = MIMEMultipart()#msg = MIMEText(mail_content, "plain", 'utf-8')msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = sender_qq_mail
msg["To"] = Header("接收者测试", 'utf-8') ## 接收者的别名#邮件正文内容msg.attach(MIMEText(mail_content, 'html', 'utf-8'))
# 构造附件1，传送当前目录下的 test.txt 文件att1 = MIMEText(open('attach.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'# 这里的filename可以任意写，写什么名字，邮件中显示什么名字att1["Content-Disposition"] = 'attachment; filename="attach.txt"'msg.attach(att1)
# 构造附件2，传送当前目录下的 runoob.txt 文件att2 = MIMEText(open('yiibai.txt', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'att2["Content-Disposition"] = 'attachment; filename="yiibai.txt"'msg.attach(att2)#ssl登录smtp = SMTP_SSL(host_server)#set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式smtp.set_debuglevel(1)
smtp.ehlo(host_server)
smtp.login(sender_qq, pwd)

smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
smtp.quit()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header


# 设置SMTP服务器以及登录信息
SERVER = {
    'host': "smtp.qq.com",
    'port': 465
}

USER = {
    "email": "1047924016@qq.com",  # 邮箱登录账号
    "password": "******************"  # 发送人邮箱的授权码
}


class PersonMail(object):
    def __init__(self, receivers, sender=USER["email"]):
        self.From = sender
        self.To = receivers
        self.msg = ''

    def write_msg(self, subject, content):
        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        self.msg = MIMEText(content, 'plain', 'utf-8')
        self.msg['From'] = Header(self.From)
        self.msg['To'] = Header(str(";".join(self.To)))
        self.msg['Subject'] = Header(subject)

    def send_email(self):
        try:
            smtp_client = smtplib.SMTP_SSL(SERVER["host"], SERVER["port"])
            smtp_client.login(USER["email"], USER["password"])
            smtp_client.sendmail(self.From, self.To, self.msg.as_string())
            smtp_client.quit()
            return 1
        except smtplib.SMTPException as e:
            print("error", e)
            return 0


if __name__ == '__main__':
    def test():
        receivers = ["yeygaooo@163.com"]
        pengpeng_email = PersonMail(receivers)
        pengpeng_email.write_msg("Test subject", "这是单纯地测试发送")
        result = pengpeng_email.send_email()
        print(result)

    test()
