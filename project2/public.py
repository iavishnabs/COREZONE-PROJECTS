from flask import *
from database import *
from admin import adminpage
from user import userpage

public_var = Blueprint('public_var',__name__) # Creating special variable


@public_var.route('/')
def homepage():
	return render_template("index.html")

@public_var.route('/user_reg',methods=['get','post'])
def user_reg():
	if 'submit' in request.form:
		fname = request.form['fname']
		lname = request.form['lname']
		uname = request.form['uname']
		passw = request.form['pasw']
		email = request.form['email']
		phn = request.form['phn'] 
		place = request.form['place']
		print(fname, lname)

		q="INSERT INTO `login_tbl` VALUES(null,'%s','%s','user')"%(uname,passw) 
		res = insert(q)

		q = "INSERT INTO `reg_tbl` VALUES(null,'%s','%s','%s','%s','%s','%s')"%(res,fname,lname,email,phn,place)
		insert(q)
		return redirect(url_for('public_var.homepage'))
	return render_template("register.html")

@public_var.route("/login",methods=['get','post'])
def user_login():
	
	if 'submit' in request.form:
		username = request.form['uname'] 
		passw = request.form['pasw']
		q = "SELECT * FROM `login_tbl` WHERE username ='%s' and password='%s' "%(username,passw)
		res = select(q)
		if res:
			if res[0]['usertype'] == "admin":
				return redirect(url_for('admin.adminpage'))
			elif  res[0]['usertype'] == "user":
				session["lid"]=res[0]["login_id"]
				return redirect(url_for('user.userpage')) 
			else:
				return redirect(url_for('public_var.user_login'))
		else:
			return '''<script>alert('invalid usernme or password');window.location='/login'</script>'''

	return render_template("login.html")