from flask import *
import uuid
from database import *

admin = Blueprint('admin',__name__) 

@admin.route('/admin')
def adminpage():
	return render_template("admin.html") 

@admin.route('/admin_category_add',methods=['get','post'])
def add_category():
	data={}
	q = "SELECT * FROM `category`"
	data['view'] = select(q)

	if 'add_cat' in request.form:
		cname = request.form['cname']
		q = "INSERT INTO `category` VALUES (null,'%s')"%(cname)
		res = insert(q)
		return redirect(url_for("admin.add_category")) 

	# delete update category	
	if "action" in request.args:
		action=request.args['action']
		cid=request.args['cid']
	else:
		action=None

	# delete category	
	if action=="delete": 
		q="DELETE FROM category WHERE cid='%s'"%(cid)
		delete(q)
		return redirect(url_for("admin.add_category"))

	return render_template("admin/cat_add.html",data=data)

@admin.route('/update_category/<int:cid>', methods=['get', 'post'])
def update_category(cid):
	data = {}
	q = "select * from `category` where `cid`='%s'"%(cid)
	data['view'] = select(q)

	if 'update_cat' in request.form:
		cname = request.form['cname']
		q = "update `category` set `cname`='%s' where `cid`='%s'"%(cid,cname)
		update(q)
		return redirect(url_for('admin.add_category')) 

	qc = "select * from `category`"
	data['view_all'] = select(qc)

	return render_template("update_category.html",data=data)

@admin.route("/admin_product_manage", methods=['get','post'])
def manage_product():
	data = {}
	catgs = "select * from `category`"
	data['view'] = select(catgs)

	pdts = "select * from product inner join category using (cid)"
	data['viewp'] = select(pdts)
	
	if "action" in request.args:
		action=request.args['action']
		pid=request.args['pid']
	else:
		action=None

	if action == "delete":
		delq="DELETE FROM product WHERE pid='%s'"%(pid)
		delete(delq)
		return redirect(url_for("admin.manage_product"))

	if action == "update":
		q = "select * from product where pid='%s'"%(pid)
		res = select(q)
		data['updates'] = res

	if 'add_prod' in request.form:
		category = request.form['catg']
		pname =  request.form['pname']
		desc =  request.form['desc']
		price =   request.form['price']
		img = request.files['img']
		path = "static/images/"+ str(uuid.uuid4())+img.filename
		img.save(path) 

		q = "INSERT INTO `product` VALUES (null,'%s','%s','%s','%s','%s')"%(category,pname,desc,price,path)
		insert(q)
		return redirect(url_for("admin.manage_product"))

	if "update" in request.form:
		catg = request.form['catg']
		pname = request.form['pname']
		descrp = request.form['descrp']
		price = request.form['price']
		img=request.files['img']
		path = "static/images/"+ str(uuid.uuid4())+img.filename
		img.save(path)

		upq = "update product set `cid`='%s', `pname`='%s',`descrp`='%s',`price`='%s',`img`='%s' where `pid`='%s'"%(catg,pname,descrp,price,path,pid)
		res=update(upq)
		return redirect(url_for("admin.manage_product"))
	
	return render_template("admin/prod_add.html",data=data)

@admin.route('/users_list')
def users_list():
	data = {}
	q = "select * from `reg_tbl`"
	data['view']=select(q)
	return render_template("users_list.html",data=data)

