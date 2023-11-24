@userxx.route('/userpayment', methods=['get', 'post'])
def userpaymenty():
    dataa = {}
    total_amountt = request.args['total_amount']

    if 'payment' in request.form:
        account_number = request.form['acountnumber']
        card_number = request.form['cardnumber']
        cvv_number = request.form['cvv']
        pin_number = request.form['pinnumber']
        amount = request.form['amount']

        kj = "select * from bank_acount where account_no='%s' and pin_no='%s' and card_no='%s' and cvv='%s'" % (
            account_number, pin_number, card_number, cvv_number)
        res = select(kj)
        
        if res:
            kl = "SELECT * FROM `cart`INNER JOIN `products`USING(`product_id`) where user_id='%s'" % (session['user_id'])
            dataa['viewcart'] = select(kl)
            k = "insert into order_master values(null,'%s',curdate(),'%s','paid')" % (session['user_id'], amount)
            om_id = insert(k)
            if dataa['viewcart']:
                total_amount = 0
                for i in dataa['viewcart']:
                    shop_id = int(i['shop_id'])
                    product_id = int(i['product_id'])
                    qty = int(i['quantity'])
                    price = int(i['price'])
                    total_amount += qty * price
                    h = "insert into order_details values(null,'%s','%s','%s','%s','%s')" % (
                        om_id, shop_id, product_id, price, qty)
                    insert(h)
                    j = "delete from cart where product_id='%s' and user_id='%s'" % (product_id, session['user_id'])
                    delete(j)
                    nm = "update stock set quantity=quantity-'%s' where product_id='%s'" % (qty, product_id)
                    update(nm) 
                hjk = "insert into payment values(null,'%s','%s','%s','paid',curdate())" % (
                    om_id, session['user_id'], total_amountt) 
                select(hjk)
                p="select * from user inner join login using(login_id) where user_id='%s'"%(session['user_id'])
                vl=select(p) 
                print(vl)
                for i in vl:
                    email = i['email']

                pwd="name:"+i['firstname']+"amount:"+total_amountt
                
                try:
                    gmail = smtplib.SMTP('smtp.gmail.com', 587)
                    gmail.ehlo()
                    gmail.starttls()
                    gmail.login('hariharan0987pp@gmail.com', 'rjcbcumvkpqynpep')  
                except Exception as e:
                    print("Couldn't setup email!!" + str(e))

                pwd = MIMEText(pwd)

                pwd['Subject'] = 'Your order details:'

                pwd['To'] = email

                pwd['From'] = 'hariharan0987pp@gmail.com'

                try:
                    gmail.send_message(pwd)

                    flash("EMAIL SEND SUCCESFULLY")

                except Exception as e:
                    print("COULDN'T SEND EMAIL", str(e))
                else:
                    flash("INVALID DETAILS")
                    flash('ADDED...')

        flash("Payment Success..........!")
        return redirect(url_for('user.userviewcartt'))
    return render_template('user_payment.html', total_amount=total_amountt, data=dataa)