from flask import *

user =  Blueprint('user',__name__)

@user.route('/user_index')

def userpage():
	return render_template("us_index.html")