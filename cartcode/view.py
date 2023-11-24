def userviewcartt():
    dataa = {}
    total_amount = 0
    op = "select * from cart where user_id='%s'" % (session['user_id'])
    res1 = select(op)
    if res1:
        c_id = res1[0]['cart_id']
        kl = "select *, `cart`.`quantity` AS oq, `stock`.`quantity` AS pq from cart inner join products using(product_id)inner join stock using(product_id) inner join shop using(shop_id) where user_id='%s'" % (session['user_id'])
        dataa['viewcart'] = select(kl)
        
        if dataa['viewcart']:
            for item in dataa['viewcart']:
                try:
                    quantity = int(item['oq'])
                    price = float(item['price'])
                    total_amount += quantity * price
                except alert:
                    pass
    if 'actionn' in request.args:
        action = request.args['actionn']
        cart_id = request.args['c_id']
        product_id = request.args['pro_id']
        price = request.args['price']
    else:
        action = None
    if action == 'decrease':
        k = "select * from cart where cart_id='%s'" % (cart_id)
        res2 = select(k)
        if res2:
            if int(res2[0]['quantity']) == 1:
                flash("Minimum product quantity should be 1")
            else:
                j = "update cart set quantity=quantity-'1' where cart_id='%s'" % (cart_id)
                update(j)
        return redirect(url_for('user.userviewcartt'))
    if action == 'increase':
        kl = "select *, stock.quantity as stockq from stock where product_id='%s'" % (product_id)
        res4 = select(kl)
        stock1111 = res4[0]['stockq']
        l = "select *, cart.quantity as otockq from cart where cart_id='%s'" % (cart_id)
        res3 = select(l)
        if res3:
            qty11111 = res3[0]['otockq']
            if stock1111 == qty11111:
                flash("Cart Quantity Must be Less Than Stock.")
            else:
                h = "update cart set quantity=quantity+'1' where  cart_id='%s'" % (cart_id)
                update(h)
        return redirect(url_for('user.userviewcartt'))
    if 'actionn1' in request.args:
        action = request.args['actionn1']
        cart_id = request.args['c_id']
    else:
        action = None
    if action == 'remove':
        l = "delete from cart where cart_id='%s'" % (cart_id)
        delete(l)
        flash("Removed..........!")
        return redirect(url_for('user.userviewcartt'))
    return render_template('user_view_cart.html', data=dataa, total_amount=total_amount)