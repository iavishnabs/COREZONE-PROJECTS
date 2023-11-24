from flask import *

import smtplib
from email.mime.text import MIMEText

admin = Blueprint("admin",__name__)

@admin.route('/')
def index():
	return render_template("index.html")


# EMAIL NOTIFICATION FUNCTION
@admin.route("/mytry")
def mytry():
	try:
			gmail = smtplib.SMTP('smtp.gmail.com', 587)
			gmail.ehlo()
			gmail.starttls()
			gmail.login('encycodepediayt@gmail.com','lizxhqfbstwyvjua')
	
			print("hi")
			msg = MIMEText("vjhjjgjhgj")

			msg['Subject'] = 'Your Username and password is:'

			msg['To'] = "riss.mamtha@gmail.com"

			msg['From'] = 'encycodepediayt@gmail.com'

		
			gmail.send_message(msg)

			print("EMAIL SEND SUCCESFULLY")

		
	except Exception as e:
		print("Couldn't setup email!!"+str(e))
	return "ok"