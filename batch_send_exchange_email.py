# 使用exchangelib实现Exchange邮件发送
# 1. 使用py
from exchangelib import DELEGATE, Account, Credentials, Message, Mailbox, HTMLBody


def Email(to, subject, body):
    creds = Credentials(
        username='wei.yw.ye',
        password='Gaochan@199008196'
    )
    account = Account(
        primary_smtp_address='wei.yw.ye@fih-foxconn.com',
        credentials=creds,
        autodiscover=True,
        access_type=DELEGATE
    )
    message = Message(
        account=account,
        subject=subject,
        body=HTMLBody(body),
        to_recipients=[Mailbox(email_address=to)]
    )

    message.attach()
    message.send()

message = "我是一个测试邮件"
Email("1047924016@qq.com","Python测试",message)