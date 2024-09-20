import smtplib as smtp

connection = smtp.SMTP_SSL('smtp.gmail.com', 465)
    
email_addr = 'deevsurya14@gmail.com'
email_passwd = 'fqhw xeie oajm wspc'
connection.login(email_addr, email_passwd)
connection.sendmail(from_addr=email_addr, to_addrs='gmaheswaranmca@gmail.com', msg="Surya N")
connection.close()
print('Mail sent successfully')