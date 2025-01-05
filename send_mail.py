import smtplib
from email.mime.text import MIMEText

def send_mail(customer,dealer,rating,comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login=""
    password = ''#login and password mailtrap
    message = f"<h3>New feedback Submission</h3><ul><li>Customer:{customer}</li><li>Dealer:{dealer}</li><li>Rating:{rating}</li><li>Comments:{comments}</li></ul>"


    sender_email=''#my smtp username
    receiver_email=''#my mail because i used demoemail domain
    msg=MIMEText(message,'html')
    msg['Subject']='Lexus Feedback'
    msg['From']=sender_email
    msg['To']= receiver_email
    
    #send email
    with smtplib.SMTP(smtp_server,port)as server:
        server.login(login,password)
        server.sendmail(sender_email, receiver_email,msg.as_string())