class Email:


    @staticmethod
    def sendEmail(subject,msg,recieverEmail):
    	try:
    		server = smtplib.SMTP('smtp.gmail.com:587')
    		server.ehlo()
    		server.starttls()
    		server.login(conf.email,conf.pas)
    		server.sendmail(conf.email, recieverEmail ,msg)
    		server.quit()
    		print("Email was sent successfuly")
    	except:
    		print("Error in sending the email")
