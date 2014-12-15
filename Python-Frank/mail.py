import smtplib
from email.mime.text import MIMEText
totalGrade = 'test.csv'
myMailAddress = 'hahaha@gmail.com'
myMailPassword = 'ilikehaha'

def getMailContent(fileName):
	fp = open(fileName,'rb')
	fcontent =  fp.read()
	fp.close()
	return  fcontent

def sendMail(s):

	gradeFile = open(totalGrade,'rb')
	while 3 == 3:

		a = gradeFile.readline()
		if(len(a) == 0):
			break
		line = a.split(',')
		if(len(line) > 0):
			content = getMailContent('content.txt') + '\n' + getMailContent('testGrade.txt') 

			for index in range(2,9):
				if(line[index]):
					content = content + line[index] + ','
				else: 
					content = content + '0,'
			
			if(line[10]):
				content = content + line[10]	
			else:
				content = content + '0'	

			if(line[11]):
				content = content + '\n' + getMailContent('termGrade.txt') + line[11]
			else: 
				content = content + '\n' + getMailContent('termGrade.txt') + '0' 

			msg = MIMEText(content)
			msg['Subject'] = getMailContent('name.txt')
			msg['From'] = myMailAddress
			msg['To'] = line[1]
			s.sendmail(myMailAddress,[line[1],myMailAddress],msg.as_string())
		else:
			break

	gradeFile.close()

s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()

if(s.has_extn('starttls')):
	s.starttls()
	s.ehlo()
s.login(myMailAddress, myMailPassword)
sendMail(s)
s.quit()

	



