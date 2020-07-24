import pymongo
from flask import Flask,render_template,request,session
from datetime import timedelta

db=pymongo.MongoClient(host='localhost',port=27017)
mydb=db["Website"]
products=mydb.Products
reg=mydb.Register
add_to_cart=mydb.cart
adm=mydb.Admin
wl=mydb.wishlist
orders=mydb.Orders
stat=mydb.Status




record={'name':'aditi'}

app=Flask(__name__)
app.secret_key="hello"
app.permanent_session_lifetime = timedelta(days=366)
#######  add those line here

@app.route('/home')
def home():
    email=session['email']
    return render_template('main.html',email=email)
    #return render_template('base_temp.html')

@app.route('/create',methods=['POST'])
def create():
    dress_type=request.form['dress_type']
    gender=request.form['gender']
    brand=request.form['brand']
    colour=request.form['colour']
    price=int(request.form['price'])
    image=request.form['image']
    products.insert_one({'dress_type':dress_type,'gender':gender,'brand':brand,'colour':colour,'price':price,'image':image})
    return render_template('base_temp.html',image=image)

@app.route('/dress')
def dress():
    email=session['email']
    product= [i for i in products.find({'dress_type':'dress'})]
    return render_template('product_list.html',products=product,email=email)

@app.route('/ftop')
def ftop():
    email=session['email']
    product= [i for i in products.find({'dress_type':'ftop'})]
    return render_template('product_list.html',products=product,email=email)


@app.route('/saree')
def saree():
    email=session['email']
    product= [i for i in products.find({'dress_type':'saree'})]
    return render_template('product_list.html',products=product,email=email)    

@app.route('/reebok')
def reebok():
    email=session['email']
    product= [i for i in products.find({'brand':'Reebok'})]
    return render_template('product_list.html',products=product,email=email)    

@app.route('/nike')
def nike():
    email=session['email']
    product= [i for i in products.find({'brand':'Nike'})]
    return render_template('product_list.html',products=product,email=email)    

@app.route('/hm')
def hm():
    email=session['email']
    product= [i for i in products.find({'brand':'H.M'})]
    return render_template('product_list.html',products=product,email=email)    

@app.route('/puma')
def puma():
    email=session['email']
    product= [i for i in products.find({'brand':'Puma'})]
    return render_template('product_list.html',products=product,email=email)    

@app.route('/gap')
def gap():
    email=session['email']
    product= [i for i in products.find({'brand':'Gap'})]
    return render_template('product_list.html',products=product,email=email)    

@app.route('/pant')
def pant():
    email=session['email']
    product= [i for i in products.find({'brand':'Pantaloons'})]
    return render_template('product_list.html',products=product,email=email)    

@app.route('/lui')
def lui():
    email=session['email']
    product= [i for i in products.find({'brand':'Louis Vuitton'})]
    return render_template('product_list.html',products=product,email=email)    

@app.route('/f')
def f():
    email=session['email']
    product= [i for i in products.find({'gender':'F'})]
    #l = [i for i in products.find({'gender':'F','price':{'$and':[{'$gt':price-500,'$lt':price+500}]}})]
    return render_template('product_list.html',products=product,email=email)    


@app.route('/m')
def m():
    email=session['email']
    product= [i for i in products.find({'gender':'M'})]
    #l = [i for i in products.find({'gender':'F','price':{'$and':[{'$gt':price-500,'$lt':price+500}]}})]
    return render_template('product_list.html',products=product,email=email)    


@app.route('/yellow')
def yellow():
    email=session['email']
    product= [i for i in products.find({'colour':'yellow'})]
    return render_template('product_list.html',products=product,email=email)    

@app.route('/red')
def red():
    email=session['email']
    product= [i for i in products.find({'colour':'red'})]
    return render_template('product_list.html',products=product,email=email)    

@app.route('/blue')
def blue():
    email=session['email']
    product= [i for i in products.find({'colour':'blue'})]
    return render_template('product_list.html',products=product,email=email)    

@app.route('/black')
def black():
    email=session['email']
    product= [i for i in products.find({'colour':'black'})]
    return render_template('product_list.html',products=product,email=email)    

@app.route('/2500')
def two():
    email=session['email']
    product= [i for i in products.find({'price':{'$lt':2500}})]
    return render_template('product_list.html',products=product,email=email)

@app.route('/4000')
def four():
    email=session['email']
    product= [i for i in products.find({'price':{'$lt':4000,'$gt':2500}})]
    return render_template('product_list.html',products=product,email=email)

@app.route('/6000')
def six():
    email=session['email']
    product= [i for i in products.find({'price':{'$lt':6000,'$gt':4000}})]
    return render_template('product_list.html',products=product,email=email)

@app.route('/8000')
def eight():
    email=session['email']
    product= [i for i in products.find({'price':{'$lt':8000,'$gt':6000}})]
    return render_template('product_list.html',products=product,email=email)

@app.route('/adminhome')
def adminhome():
    email=session['email']
    return render_template('adminhome.html',email=email)

@app.route('/admin',methods=['POST','GET'])
def admin():
    email=session['email']
    authid=request.form['authid']
    if(authid=='12345'):
        return render_template('adminhome.html',email=email,auth=None)
    else:
        return render_template('adminhome.html',email=email,auth='The Authentication ID is Incorrect')
    # users=[i for i in reg.find()]
    # return render_template('admin.html',name='users are {}'.format(users))


@app.route('/users',methods=['POST','GET'])
def users():
    email=session['email']
    users=[i for i in reg.find()]
    return render_template('user.html',user=users,email=email)    

@app.route('/remove+<image>+<dress_type>+<brand>+<colour>+<price>+<gender>')
def remove(image,dress_type,brand,colour,price,gender):
    email=session['email']
    add_to_cart.remove({'image':image,'dress_type':dress_type,'brand':brand,'colour':colour,'price':price,'gender':gender})
    l = [i for i in add_to_cart.find({'email':email})]
    sum=0
    for i in l:
        sum=sum+int(i['price'])*i['quantity']
    sub_total=sum+100  
    if(len(l)==0):
        names=[j for j in reg.find({'email':email})]
        k=names[0]
        name=k['fname']
        return render_template('nocontent.html',email=email,name=name)
    else:
        return render_template('cart.html',l=l,available=False,total=sum,email=email,sub_total=sub_total)
  
@app.route('/removewishlist+<image>+<dress_type>+<brand>+<colour>+<price>+<gender>+<quantity>+<size>')
def removewishlist(image,dress_type,brand,colour,price,gender,quantity,size):
    email=session['email']
    quantity=int(quantity)
    wl.remove({'image':image,'dress_type':dress_type,'brand':brand,'colour':colour,'price':price,'gender':gender,'quantity':quantity,'size':size})
    l = [i for i in wl.find({'email':email})]  
    if(len(l)==0):
        names=[j for j in reg.find({'email':email})]
        k=names[0]
        name=k['fname']
        return render_template('nocontent.html',email=email,name=name)
    else:
        return render_template('wishlist.html',l=l,available=False,email=email)

@app.route('/cart+<image>+<dress_type>+<brand>+<colour>+<price>+<gender>',methods=['POST'])
def cart(image,dress_type,brand,colour,price,gender):
    email=session['email']
    quantity = int(request.form['quantity'])
    size = request.form['size']
    available = [i for i in add_to_cart.find({'email':email,'image':image,'dress_type':dress_type,'brand':brand,'colour':colour,'price':price,'gender':gender}) ]
    if(len(available)==0):
        add_to_cart.insert_one({'email':email,'image':image,'dress_type':dress_type,'brand':brand,'colour':colour,'price':price,'gender':gender,'quantity':quantity,'size':size})   
        l = [i for i in add_to_cart.find({'email':email})]
        sum=0
        for i in l:
            sum=sum + int(i['price'])*(i['quantity'])
        sub_total=sum+100
        return render_template('cart.html',l=l,available=False,total=sum,email=email,sub_total=sub_total)  
    else:
        l = [i for i in add_to_cart.find({'email':email})]
        sum=0
        for i in l:
            sum=sum + int(i['price'])
        sub_total=sum+100
        return render_template('cart.html',l=l,available=True,total=sum,email=email,sub_total=sub_total)

@app.route('/cartroller')
def cartroller():
    email=session['email']
    l = [i for i in add_to_cart.find({'email':email})]    
    sum=0
    for i in l:
        sum=sum+int(i['price'])*i['quantity']
    sub_total=sum+100    
    if(len(l)==0):
        names=[j for j in reg.find({'email':email})]
        k=names[0]
        name=k['fname']
        return render_template('nocontent.html',email=email,name=name)
    else:
        return render_template('cart.html',l=l,total=sum,email=email,sub_total=sub_total)


@app.route('/wishlistaddtocart+<image>+<dress_type>+<brand>+<colour>+<price>+<gender>+<quantity>+<size>')
def wishlistaddtocart(image,dress_type,brand,colour,price,gender,quantity,size):
    email=session['email']
    quantity=int(quantity)
    add_to_cart.insert_one({'email':email,'image':image,'dress_type':dress_type,'brand':brand,'colour':colour,'price':price,'gender':gender,'quantity':quantity,'size':size})   
    wl.remove({'image':image,'dress_type':dress_type,'brand':brand,'colour':colour,'price':price,'gender':gender,'quantity':quantity,'size':size})
    l = [i for i in wl.find({'email':email})] 
    return render_template('wishlist.html',l=l,available=False,email=email) 

@app.route('/wishlist+<image>+<dress_type>+<brand>+<colour>+<price>+<gender>+<quantity>+<size>')
def wishlist(image,dress_type,brand,colour,price,gender,quantity,size):
    email=session['email']
    quantity=int(quantity)
    available = [i for i in wl.find({'email':email,'image':image,'dress_type':dress_type,'brand':brand,'colour':colour,'price':price,'gender':gender,'quantity':quantity,'size':size}) ]
    if(len(available)==0):
        wl.insert_one({'email':email,'image':image,'dress_type':dress_type,'brand':brand,'colour':colour,'price':price,'gender':gender,'quantity':quantity,'size':size})   
        add_to_cart.remove({'image':image,'dress_type':dress_type,'brand':brand,'colour':colour,'price':price,'gender':gender})
        l = [i for i in add_to_cart.find({'email':email})]
        sum=0
        for i in l:
            sum=sum+int(i['price'])*i['quantity']
        sub_total=sum+100    
        return render_template('cart.html',l=l,available=False,total=sum,email=email,sub_total=sub_total) 
    else:
        l = [i for i in add_to_cart.find({'email':email,})]
        return render_template('wishlist.html',l=l,available=True,email=email)   

@app.route('/wishlistroller')
def wishlistroller():
    email=session['email']
    l = [i for i in wl.find({'email':email})]
    if(len(l)==0):
        names=[j for j in reg.find({'email':email})]
        k=names[0]
        name=k['fname']
        return render_template('nocontent.html',email=email,name=name)
    else:
        return render_template('wishlist.html',l=l,email=email)


@app.route('/')
def signin():
    return render_template('signin.html')

@app.route('/signinform',methods=['POST','GET'])
def signinform():
    session.permanent=True
    email=request.form['email']
    password=request.form['password']
    session['email']=email
    if((email)==('admin@gmail.com') and (password)==('admin')):
        return render_template('admin.html',email=email)
    for i in reg.find():
        if((email)==i['email'] and (password)==i['pass']):
            return render_template('main.html',email=email)
    return render_template('signup.html')   

@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/signupform',methods=['POST','GET'])
def signupform():
    
    fname=request.form['fname']
    lname=request.form['lname']
    email=request.form['email']
    password=request.form['password']
    ph=request.form['ph']
    address=request.form['address']
    city=request.form['city']
    state=request.form['state']
    zip=request.form['zip']
    reg.insert_one({'fname':fname,'lname':lname,'email':email,'pass':password, 'ph':ph,'address':address,'city':city,'state':state,'zip':zip,'items':None})
    return render_template('signin.html')
   
@app.route('/logout')
def logout():
    session.pop('email',None)
    return render_template('main.html',email=None)

# @app.route('/buynow')
# def buynow():
#     email=session['email']
    
#     order=[i for i in (add_to_cart.find({'email':email}))]
#     i=order[-1]
#     email=i['email']
#     price=i['price']
#     add_to_cart.remove({'email':email})
#     names=[j for j in reg.find({'email':email})]
#     k=names[0]
#     name=k['fname']
    
#     orders.insert_one({'email':email,'price':price,'status':'Order Accepted'})   
#     return render_template('feedback.html',email=email,name=name)

@app.route('/feedback')
def feedback():
    email=session['email']
    names=[j for j in reg.find({'email':email})]
    k=names[0]
    name=k['fname']
    return render_template('feedback.html',email=email,name=name)

@app.route('/buynow')
def buynow():
    email=session['email']
    
    order=[i for i in (add_to_cart.find({'email':email}))]
    for i in order:
        email=i['email']
        image=i['image']
        price=i['price']
        orders.insert_one({'email':email,'image':image,'price':price,'status':'Pending'})   
    add_to_cart.remove({'email':email})    
    return render_template('final.html',email=email)

@app.route('/adminorders')
def adminorders():
    email=session['email']
    order=[i for i in orders.find()]
    return render_template('orders.html',orders=order,email=email)

@app.route('/accept+<email>+<price>+<image>')
def accept(email,price,image):
    orders.update_one({'image':image,'email':email,'price':price},{'$set':{'status':'Order Accepted'}})
    status='Order Accepted'
    order=[i for i in orders.find()]
    return render_template('orders.html',status=status,orders=order,email=email)

@app.route('/dispatch+<email>+<price>+<image>')
def dispatch(email,price,image):
    orders.update_one({'email':email,'image':image,'price':price},{'$set':{'status':'Dispatched'}})
    status='Dispatched'
    order=[i for i in orders.find()]
    return render_template('orders.html',status=status,orders=order,email=email)

@app.route('/deliver+<email>+<price>+<image>')
def deliver(email,price,image):
    orders.update_one({'email':email,'price':price,'image':image},{'$set':{'status':'Delivered'}})
    status='Delivered'
    order=[i for i in orders.find()]
    return render_template('orders.html',status=status,orders=order,email=email)


@app.route('/myorders')
def myorders():
    email=session['email']
    myorders=[i for i in orders.find({'email':email})]
    return render_template('myorders.html',hello=myorders,email=email)
    

if __name__ == "__main__":
    app.run(debug=True)    