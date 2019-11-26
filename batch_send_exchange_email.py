# 使用exchangelib实现Exchange邮件发送
# 1. 使用"pip3 install exchangelib"安装exchangelib
import datetime

import os
from exchangelib import DELEGATE, Account, Credentials, Message, Mailbox, Body, FileAttachment

# real send email
def Email(to, cc, subject, body, files):
    creds = Credentials(
        username='wei.yw.ye',
        password='****************'
    )
    # config exchange email account, to access server
    account = Account(
        primary_smtp_address='wei.yw.ye@fih-foxconn.com',
        credentials=creds,
        autodiscover=True,
        access_type=DELEGATE
    )
    # config email infomation：account、to reciever、cc reciever、subject、body
    message = Message(
        account=account,
        subject=subject,
        body=Body(body),
        to_recipients=[Mailbox(email_address=to)],
        cc_recipients=[Mailbox(email_address=cc)]
    )

    # add attachment
    for path in files:
        with open(r"attachment/"+path, 'rb') as f:
            myfile = FileAttachment(name=path, content=f.read())
        message.attach(myfile)

    message.send_and_save()

def loadFiles(dirPath):
    for root, dirs, files in os.walk(dirPath):
        return files

if __name__ == '__main__':
    dirPath = r"attachment"
    files = loadFiles(dirPath)
    # load
    subject_header = ""
    for f in files:
        temp = f.split("_")[1]
        print("temp is " + temp)
        subject_header = subject_header + temp + "&"
    if(subject_header.endswith("&")):
        subject_header = subject_header[:-1]
    print("subject_header is " + subject_header)
    today = datetime.date.today()
    formatted_today = today.strftime('%m')
    print("today is " + formatted_today);
    to_reciever = "1047924016@qq.com"
    cc_reciever = "yeygaooo@163.com"
    split = to_reciever.split("@")
    message = "Dear All\n" \
              "\n" \
              "Please find cost center report for P01 FY20 thanks.\n" \
              "\n" \
              "Mit freundlichen Gruben\n" \
              "Chan Gao"
    subject = "830306&830301 Cost center report P" + formatted_today + ".20"
    print("subject is " + subject);
    Email(to_reciever, cc_reciever, subject, message, files)
