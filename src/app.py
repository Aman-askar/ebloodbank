from flask import *
from src.dbconnection import *
app=Flask(__name__)
app.secret_key="qaaaa"

@app.route('/add_emergency')
def add_emergency():
    return render_template("add_emergncy.html")

@app.route('/add_stock',methods=['post'])
def add_stock():
    return render_template("add_stock.html")

@app.route('/admin_home')
def admin_home():
    return render_template("admin_home.html")

@app.route('/view_stock')
def view_stock():
    bid = request.args.get('blid')
    session['blid'] = bid
    return render_template("view_stock.html")

@app.route('/donate')
def donate():
    id = request.args.get('id')
    session['hid'] = id
    return render_template("donateblood.html")

@app.route('/donateblood', methods=['post'])
def donateblood():
    grp = request.form['select']
    count = request.form['text']
    qry = "insert into donate values(null,%s,%s,%s,'donation',%s,curdate())"
    val = session['hid'], session['lid'], grp, count
    print(val)
    iud(qry, val)
    return '''<script>alert("donated");window.location="/userviewblood_bank"</script>'''

@app.route('/donation_responce')
def donation_responce():
    q = "SELECT `donate`.* FROM `donate` JOIN `bloodbank` ON `bloodbank`.`bank_id`=`donate`.`hlid` WHERE `bloodbank`.`bank_loginid`=%s"
    res = selectall2(q,session['lid'])
    return render_template("donation_responce.html", val=res)

@app.route('/searchstock',methods=['post'])
def searchstock():
    blood = request.form['select']
    qry = "SELECT `stock`.* FROM `stock` JOIN `bloodbank` ON`stock`.`blood_bank_loginid`=`bloodbank`.`bank_loginid` WHERE `stock`.`blood_bank_loginid`=%s AND `stock`.`blood_group`=%s"
    val = (session['blid'], blood)
    res = selectall2(qry, val)
    return render_template("view_stock.html", val=res)

@app.route('/userviewblood_bank')
def userviewblood_bank():
    qry = "SELECT * FROM `bloodbank`"
    res = selectall(qry)
    return render_template("user view blood_bank.html", val=res)

@app.route('/acceptbank')
def acceptbank():
    id = request.args.get('id')
    qry = "UPDATE `login` SET `type`='bloodbank' WHERE `login_id`=%s"
    val = str(id)
    iud(qry, val)
    return '''<script>alert("accepted");window.location="/blood_bank"</script>'''

@app.route('/rejectbank')
def rejectbank():
    id = request.args.get('id')
    qry = "UPDATE `login` SET `type`='rejected' WHERE `login_id`=%s"
    val = str(id)
    iud(qry, val)
    return '''<script>alert("rejected");window.location="/blood_bank"</script>'''

@app.route('/acceptuser')
def acceptuser():
    id = request.args.get('id')
    qry = "UPDATE `login` SET `type`='blocked' WHERE `login_id`=%s"
    val = str(id)
    iud(qry, val)
    return '''<script>alert("blocked");window.location="/view_users"</script>'''

@app.route('/rejectuser')
def rejectuser():
    id = request.args.get('id')
    qry = "UPDATE `login` SET `type`='user' WHERE `login_id`=%s"
    val = str(id)
    iud(qry, val)
    return '''<script>alert("unblocked");window.location="/view_users"</script>'''

@app.route('/emergencyapprove')
def emergencyapprove():
    id = request.args.get('id')
    print(id)
    qry = "UPDATE `emergency_alert` SET `status`='approve' WHERE `emergency_id`=%s"
    val = str(id)
    iud(qry, val)
    qry1 = "INSERT INTO `responce` VALUES (NULL,%s,%s,CURDATE(),'accepted')"
    val1 = (session['lid'],id)
    iud(qry1, val1)
    return '''<script>alert("approved");window.location="/view_emergency_msg"</script>'''

@app.route('/emergencyreject')
def emergencyreject():
    id=request.args.get('id')
    qry="UPDATE `emergency_alert` SET `status`='reject' WHERE `emergency_id`=%s"
    val=str(id)
    iud(qry,val)
    qry1 = "INSERT INTO `responce` VALUES (NULL,%s,%s,CURDATE(),'rejected')"
    val1 = (session['lid'], id)
    iud(qry1, val1)
    return '''<script>alert("rejected");window.location="/view_emergency_msg"</script>'''

@app.route('/bloodbank_home')
def bloodbank_home():
    return render_template("bloodbank_home.html")

@app.route('/blood_bank')
def blood_bank():
    q="SELECT `bloodbank`.*,`login`.`type` FROM `bloodbank` JOIN `login` ON `bloodbank`.`bank_loginid`=`login`.`login_id` WHERE `login`.`type`='pending'"
    res=selectall(q)
    return render_template("blood_bank.html",val=res)

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/manage_stockinfo')
def manage_stockinfo():
    q="SELECT * FROM `stock` WHERE `blood_bank_loginid`=%s"
    v=session['lid']
    s=selectall2(q,v)
    return render_template("manage_stockinfo.html",val=s)

@app.route('/reply')
def reply():
    id = request.args.get('id')
    session['cid']=id
    return render_template("reply.html")

@app.route('/sendreply',methods=['post'])
def sendreply():
    reply = request.form['text']
    qry = "update complaint set reply=%s where cmp_id=%s"
    val = (reply, session['cid'])
    iud(qry, val)
    return redirect('view_complaint')

@app.route('/send_complaint')
def send_complaint():
    return render_template("send_complaint.html")

@app.route('/send_emergency_alert')
def send_emergency_alert():
    return render_template("send_emergency_alert.html")

@app.route('/send_emergency_msg')
def send_emergency_msg():
    return render_template("send_emergency_msg.html")

@app.route('/send_feedback')
def send_feedback():
    return render_template("send_feedback.html")

@app.route('/send_feedbacks' ,methods=['post'])
def send_feedbacks():
    feedbk=request.form['feedback']
    qry="insert into feedback values(null,curdate(),%s,%s)"
    val=(session['lid'],feedbk)
    iud(qry,val)
    return '''<script>alert("feedback sent");window.location = "/send_feedback"</script>'''

@app.route('/add_emergency_alert', methods=['post'])
def add_emergency_alert():
    bloodgroup=request.form['select']
    count=request.form['textfield2']
    qry="insert into emergency_alert values(null,%s,curdate(),%s,%s,'pending')"
    val=(session['lid'],bloodgroup,count)
    iud(qry,val)
    return '''<script>alert("sent sucessfully");window.location="/bloodbank_home"</script>'''

@app.route('/user_home')
def user_home():
    return render_template("user_home.html")

@app.route('/sent_feedback', methods=['post'])
def sent_feedback ():
    feedback = request.form['text']
    qry = "insert into feedback values(null,curdate(),%s,%s)"
    val = (session['lid'],feedback)
    iud(qry, val)
    return '''<script>alert("sent feedback sucessfully");window.location="/user_home"</script>'''
    return render_template("user_home.html")

@app.route('/user_registration')
def user_registration():
    return render_template("user_registration.html")

@app.route('/hospital_registration')
def hospital_registration():
    return render_template("hospital_registration.html")

@app.route('/view_bloodstatus')
def view_bloodstatus():
    return render_template("view_bloodstatus.html")

@app.route('/search_bloodstatus',methods=['post'])
def search_bloodstatus():
    group=request.form['select']
    print(group)
    qry="SELECT `bloodbank`.`hospital_name`,`stock`.* FROM `bloodbank` JOIN `stock` ON `bloodbank`.`bank_loginid`=`stock`.`blood_bank_loginid` WHERE `stock`.`blood_group`=%s"
    val=group
    res=selectall2(qry,val)
    return render_template("view_bloodstatus.html", val1=res)

@app.route('/send_complaints' ,methods=['post'])
def send_complaints():
    complaint=request.form['complaint']
    qry="insert into complaint values(null,curdate(),%s,%s,'pending')"
    val=(complaint, session['lid'])
    iud(qry, val)
    return '''<script>alert("complaint sent");window.location = "/send_complaint"</script>'''

@app.route('/view_complaint')
def view_complaint():
    qry="SELECT bloodbank.hospital_name, complaint.* FROM complaint JOIN bloodbank ON complaint.bank_loginid=bloodbank.bank_loginid WHERE complaint.reply='pending'"
    res=selectall(qry)
    return render_template("view_complaint.html", val=res)

@app.route('/view_details')
def view_details():
    emid = request.args.get('id')
    print(emid)
    q="SELECT `user`.*,`responce`.* FROM `responce`JOIN `user` ON `user`.`userlid`=`responce`.`ulid` WHERE `responce`.`emergid`=%s AND `responce`.`status`!='rejected'"
    res = selectall2(q, emid)
    return render_template("view_details.html", val=res)

@app.route('/view_details1')
def view_details1():
    emid=request.args.get('id')
    print(emid)
    q="SELECT * from user where userlid=%s"
    res=selectall2(q, emid)
    return render_template("view_details.html", val=res)

@app.route('/user_accept')
def user_acccept():
    id = request.args.get('id')
    qry = "UPDATE `responce` SET status ='accepted' WHERE `rid`=%s"
    iud(qry, id)
    return '''<script>alert("accepted");window.location="/view_user_responce"</script>'''

@app.route('/user_reject')
def user_reject():
    id = request.args.get('id')
    qry ="UPDATE `responce` SET status ='rejected' WHERE `rid`=%s"
    iud(qry, id)
    return '''<script>alert("rejected");window.location="/view_user_responce"</script>'''

@app.route('/accept_details')
def accept_details():
    id = request.args.get('id')
    qry ="UPDATE `responce` SET responce.status ='accepted' WHERE `userid`=%s"
    iud(id, qry)
    return '''<script>alert("accepted");window.location="/blood_bank"</script>'''

@app.route('/view_donation_history')
def view_dontion_history():
    qry = "SELECT `emergency_alert`.*, `responce`.*,`bloodbank`.* FROM `emergency_alert` JOIN `responce` ON `emergency_alert`.`emergency_id`=`responce`.`emergid` JOIN `bloodbank` ON `bloodbank`.`bank_loginid`=`emergency_alert`.`lid` WHERE `responce`.`ulid`=%s"
    res = selectall2(qry,session['lid'])
    return render_template("view_donation_history.html", val=res)

@app.route('/view_emergency_msg')
def view_emergency_msg():
    qry = "SELECT `bloodbank`.`hospital_name`,`emergency_alert`.* FROM `emergency_alert` JOIN `bloodbank` ON `bloodbank`.`bank_loginid`=`emergency_alert`.`lid` WHERE `emergency_alert`.`status`='pending'"
    res = selectall(qry)
    return render_template("view_emergency_msg.html", val=res)

@app.route('/view_feedback')
def view_feedback():
    qry="SELECT bloodbank.hospital_name, `feedback`.* FROM `feedback` JOIN bloodbank ON `feedback`.bank_loginid=bloodbank.bank_loginid "
    res=selectall(qry)
    return render_template("view_feedback.html", val=res)

@app.route('/view_more_details')
def view_more_details():
    return render_template("view_more_details.html")

@app.route('/view_reply')
def view_reply():
    qry="SELECT * FROM `complaint` WHERE `bank_loginid`=%s"
    res=selectall2(qry, session['lid'])
    return render_template("view_reply.html",val=res)

@app.route('/view_user_responce')
def view_user_responce():
    qry="SELECT `emergency_alert`.*,`user`.* FROM `emergency_alert` JOIN `responce` ON `responce`.`emergid`=`emergency_alert`.`emergency_id` JOIN `user` ON `user`.`userlid`=`responce`.`ulid` WHERE `emergency_alert`.`lid`=%s"
    res=selectall2(qry, session['lid'])
    return render_template("view_user_responce.html", val=res)

@app.route('/emergency_details')
def emergency_details():
    qry="SELECT * FROM `emergency_alert` where lid=%s"
    res=selectall2(qry, session['lid'])
    return render_template("emergency_details.html", val=res)

@app.route('/view_user_responce1')
def view_user_responce1():
    qry="select `date`,`blood`,`count`,`status` ,`ulid` FROM `donate` "
    res=selectall2(qry,session['lid'])
    print(res)
    return render_template("view_user_responce.html", val=res)

@app.route('/view_users')
def view_users():
    qry="SELECT `user`.*,`login`.`type` FROM `user` JOIN `login` ON `user`.`userlid`=`login`.`login_id`"
    res=selectall(qry)
    return render_template("view_users.html",val=res)

@app.route('/login1',methods=['post'])
def login1():
    uname = request.form['username']
    pswd = request.form['password']
    qry = 'select * from login where username = %s and password = %s'
    val = (uname, pswd)
    res = selectone(qry, val)
    if res is None:
        return '''<script>alert("invalid");window.location="/"</script>'''
    elif res[3] == 'admin':
        session['lid'] = res[0]
        return '''<script>alert("Welcome admin");window.location = "/admin_home"</script>'''
    elif res[3] == 'user':
        session['lid'] = res[0]
        return '''<script>alert("Welcome user");window.location = "/user_home"</script>'''
    elif res[3] == 'bloodbank':
        session['lid'] = res[0]
        return '''<script>alert("Welcome bloodbank");window.location = "/bloodbank_home"</script>'''
    else:
        return '''<script>alert("invalid");window.location = "/"</script>'''

@app.route('/hospitalreg',methods=['post'])
def hospitalreg():
    hname = request.form['hospitalname']
    place = request.form['place']
    post = request.form['post']
    pin = request.form['pin']
    phone = request.form['phone']
    email = request.form['email']
    uname = request.form['username']
    pswd = request.form['password']
    qry = "insert into login values(NULL, %s, %s, 'pending')"
    val = (uname, pswd)
    id = iud(qry, val)
    qry1 = "insert into bloodbank values(NULL, %s,%s,%s,%s,%s,%s,%s)"
    val1 = (hname, place, post, pin, phone, email, str(id))
    iud(qry1, val1)
    return '''<script>alert("registered");window.location="/"</script>'''

@app.route('/userreg',methods=['post'])
def userreg():
    fname = request.form['firstname']
    lname = request.form['lastname']
    bldgrp = request.form['blood_group']
    place = request.form['place']
    post = request.form['post']
    pin = request.form['pin']
    phone = request.form['phone']
    email = request.form['email']
    uname = request.form['username']
    pswd = request.form['password']
    qry = "insert into login values(NULL, %s, %s, 'user')"
    val = (uname, pswd)
    id = iud(qry, val)
    qry1 = "insert into user values(NULL, %s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1 = (str(id), fname, lname, bldgrp, place, post, pin, phone, email)
    iud(qry1, val1)
    return '''<script>alert("registered");window.location="/"</script>'''

@app.route('/add_bloodbank', methods=['post'])
def add_bloodbank():
    hname = request.form['hospitalname']
    place = request.form['place']
    post = request.form['post']
    pin = request.form['pin']
    phone = request.form['phone']
    email = request.form['email']
    uname = request.form['username']
    pswd = request.form['password']
    qry = "insert into login values(NULL, %s, %s, 'pending')"
    val = (uname, pswd)
    id = iud(qry, val)
    qry1 = "insert into bloodbank values(NULL,%s,%s,%s,%s,%s,%s,%s) "
    val1 = (hname, place, post, pin, phone, email, str(id))
    iud(qry1, val1)
    return '''<script>alert("registered");window.location="/"</script>'''

@app.route('/add_stocks', methods=['post'])
def add_stocks():
    opos = request.form['select']
    stock=request.form['text']
    qry1 = "insert into stock values(NULL,%s,%s,%s) "
    val1 = (session['lid'],opos,stock)
    iud(qry1, val1)
    return '''<script>alert("STOCK ADDED");window.location="/manage_stockinfo"</script>'''

@app.route('/update_stocks', methods=['post'])
def update_stocks():
    opos = request.form['select']
    stock=request.form['text']
    qry = "update stock set blood_group =%s,stock=%s where stock_id=%s "
    val=(opos,stock,session['sid'])
    iud(qry,val)
    return '''<script>alert("Stock updated");window.location="/manage_stockinfo"</script>'''

@app.route('/delete_stock')
def delete_stock():
    id = request.args.get('id')
    qry="delete from stock where stock_id=%s"
    iud(qry,id)
    return '''<script>alert("Stock deleted");window.location="/manage_stockinfo"</script>'''

@app.route('/edit_stock')
def edit_stock():
    id = request.args.get('id')
    session['sid']=id
    qry="SELECT * FROM `stock` WHERE  `stock`.`stock_id`=%s"
    res=selectone(qry,str(id))
    # res="select * from stock_id"
    return render_template("edit_stock.html",val=res)

app.run(debug=True)



