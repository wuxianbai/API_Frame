import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender, pwd, receiver, smtpserver, port, report_file):
    with open(report_file, 'rb') as f:
        mail_body = f.read()

    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = '二维码自动化测试'
    msg['from'] = sender
    msg['to'] = pwd
    msg.attach(body)

    att = MIMEText(open(report_file, 'rb').read(), _subtype='base64', _charset='utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment; filename= "report.html"'
    msg.attach(att)

    try:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
    except:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver, port)

    smtp.login(sender, pwd)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('邮件已经发送完成')

if __name__ == '__main__':
    sender = '454762930@qq.com'
    pwd = 'iyayyxtpocqjcacb'
    receiver = '454762930@qq.com'
    smtpserver = 'smtp.qq.com'
    port = 465
    report = '../report/report.html'
    send_email(sender,pwd,receiver,smtpserver,port,report)