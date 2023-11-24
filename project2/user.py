from flask import *
from database import *

user =  Blueprint('user',__name__)
@user.route('/user_index')

def userpage():
	data={}
	pdts = "SELECT * FROM `product` INNER JOIN `category` USING (cid)"
	data['viewp'] = select(pdts)
	return render_template("us_index.html",data=data)