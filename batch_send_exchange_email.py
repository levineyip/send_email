import datetime
import os

from exchangelib import DELEGATE, Account, Credentials, Message, Mailbox, Body, FileAttachment


# real send email
def Email(to, cc, subject, body, files):
    creds = Credentials(
        username='wei.yw.ye',
        password='Gaochan@199008196'
    )
    # config exchange email account, to access server
    account = Account(
        primary_smtp_address='wei.yw.ye@fih-foxconn.com',
        credentials=creds,
        autodiscover=True,
        access_type=DELEGATE
    )
    # config email infomation：account、to reciever、cc reciever、subject、body
    to_recipients = list()
    cc_recipients = list()
    for t in to:
        to_recipients.append(Mailbox(email_address=t))
    for c in cc:
        cc_recipients.append(Mailbox(email_address=c))

    message = Message(
        account=account,
        subject=subject,
        body=Body(body),
        to_recipients=to_recipients,
        cc_recipients=cc_recipients
    )

    if(files != None):
        # add attachment
        for path in files:
            with open(r"attachment/" + path, 'rb') as f:
                myfile = FileAttachment(name=path, content=f.read())
                message.attach(myfile)

    message.send_and_save()


def loadFiles(dirPath):
    for root, dirs, files in os.walk(dirPath):
        return files


if __name__ == '__main__':
    # 发送邮件的份数和to_recievers的数组长度一致
    # 每一组total_to_recievers必须和total_cc_recievers对应
    total_to_recievers = [
        ["1047924016@qq.com"],
        ["yeygaooo@163.com"]
    ]
    total_cc_recievers = [
        ["yeygaooo@163.com"],
        ["1047924016@qq.com"]
    ]

    dirPath = r"attachment"
    files = loadFiles(dirPath)
    # load
    subject_header = ""
    if(files != None):
        for f in files:
            temp = f.split("_")[1]
            print("temp is " + temp)
            subject_header = subject_header + temp + "&"
        if (subject_header.endswith("&")):
            subject_header = subject_header[:-1]
    else:
        subject_header = "None"
    print("subject_header is " + subject_header)
    today = datetime.date.today()
    formatted_today = today.strftime('%m')
    print("today is " + formatted_today);
    message = "Dear All\n" \
              "\n" \
              "Please find cost center report for P01 FY20 thanks.\n" \
              "\n" \
              "Mit freundlichen Gruben\n" \
              "Chan Gao"
    subject = subject_header + " Cost center report P" + formatted_today + ".20"
    print("subject is " + subject);

    for index, val in enumerate(total_to_recievers):
        to_recievers = val
        cc_recievers = total_cc_recievers[index]
        Email(to_recievers, cc_recievers, subject, message, files)