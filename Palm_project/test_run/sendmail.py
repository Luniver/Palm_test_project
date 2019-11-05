import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

def send_mail(file_new):
    smtpserver = 'smtp.gomo.com'

    user = 'lichenyu@gomo.com'
    password = 'Lcy1907'

    sender = 'lichenyu@gomo.com'
    receives = ['lichenyu@gomo.com']

    subjects = '手相测试报告'

    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()

    mail_information = '自动化测试已经完成，详情请见附件内容，谢谢，如有问题，请联系我。'
    body = MIMEText(mail_information,'palin','utf-8')

    msg = MIMEMultipart('related')
    msg['Subject']=Header(subjects,'utf-8').encode()
    msg['From']=sender
    msg['To']=','.join(receives)
    msg.attach(body)


    att = MIMEText(mail_body,"base64","utf-8")

    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment;filename="Palm Secret test report.html"'
    msg.attach(att)

    smtp=smtplib.SMTP_SSL(smtpserver,465)

    #HELO 向服务器标识用户身份
    smtp.helo(smtpserver)
    #服务器返回结果确认
    smtp.ehlo(smtpserver)
    #登录邮箱服务器用户名和密码
    smtp.login(user,password)

    print("开始发送邮件...")
    smtp.sendmail(sender,receives,msg.as_string())
    smtp.quit()
    print("邮件发送完成！")

if __name__ == '__main__':
    file_new = '/Users/lcy/Documents/GitHub/Palm_test_project/Palm_project/test_run/Palm Secret test report.html'
    send_mail(file_new)
