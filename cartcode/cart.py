@userxx.route("/userviewproduct",methods=['post','get'])
def userviewproductt():
	dataa={}
	if 'actionn' in request.args:
		action=request.args['actionn']
		product_id=request.args['pro_id']
		shop_id=request.args['shop_id']
		amount=request.args['amount']
	else:
		action=None
	if action=='addtocart':
		h="select * from cart where user_id='%s' and product_id='%s'"%(session['user_id'],product_id)
		r1=select(h) 
		if r1:
			p_id=r1[0]['product_id']
			c_id=r1[0]['cart_id']
			g="update cart set quantity=quantity+1 where cart_id='%s' and product_id='%s'"%(c_id,product_id)
			update(g)
			flash("added..........!")
			return redirect(url_for('user.userviewcartt'))
		else:
			hp="insert into cart values(null,'%s','%s','1')"%(session['user_id'],product_id)
			insert(hp)
			flash("added..........!")
			return redirect(url_for('user.userviewcartt'))

	product_id=request.args['pro_id']
	h="select * from products where product_id='%s'"%(product_id)
	dataa['viewpro']=select(h)
	return render_template('user_view_product.html',data=dataa)