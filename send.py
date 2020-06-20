import smtplib
from email.mime.text import MIMEText
from email.header import Header


first = ["wxxxx"]
last = ["jxxxxx"]
times = ['2']

mail_host="smtp.qq.com"  #设置服务器
mail_user="xxxxxxxxx@qq.com"    #用户名
mail_pass="xxxxxxxxx"   #口令 

with open('mail.html', 'r') as f:
    message = f.read()
message = MIMEText(message, 'html', 'utf-8')
message['From'] = Header("admin", 'utf-8')
message['To'] =  Header("全体在校生", 'utf-8')
message['Subject'] = Header("返校意愿登记", 'utf-8')

server=smtplib.SMTP_SSL(mail_host, 465) 
server.login(mail_user, mail_pass) 

for f in first:
    for l in last:
        for t in times:
            receiver = f+l+'19'+t+'@mails.ucas.ac.cn'
            try:
                server.sendmail(mail_user,[receiver],message.as_string()) 
                print (receiver+"  邮件发送成功")
            except smtplib.SMTPException:
                print (receiver+"  Error: 无法发送邮件")