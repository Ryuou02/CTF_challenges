import sqlite3
from flask import Flask, render_template, request,session,redirect,send_file
import time
import os
import uuid
app = Flask(__name__)

app.secret_key = str(uuid.uuid4())

flag = "flag{At0mic_0p3rati0ns_R_n3ce554ry}"

def execReadQuery(query,args):
    conn = sqlite3.connect('file:data.sqlite?mode=rw', uri=True)
    cursor = conn.cursor()
    cursor.execute(query,args)
    r = cursor.fetchall()
    return r
def execWriteQuery(query,args):
    conn = sqlite3.connect('file:data.sqlite?mode=rw', uri=True)
    cursor = conn.cursor()
    cursor.execute(query,args)
    conn.commit()
    conn.close()
    

message = ""
@app.route("/")
def home():
    msg=""
    print(len(session))
    if len(session) == 0:
        session['incorrect'] = 0
        session['uuid'] = str(uuid.uuid4()).replace('-',"")
        session['username'] = ""
        session['money'] = 0
        session['fetchimg'] = "/static/banker.gif"
    msg = "This is the most secure bank in history, only the one in control of the bank can change the money in everyone's accounts"
    session['fetchimg'] = "/static/banker.png"
    if session['money'] > 2500:
        msg=flag
    return render_template("index2.html", user = session['username'] , msg = msg)


@app.route("/send-money", methods=["POST","GET"])
def sendMoney():
  if(request.method == "POST"):
    if(len(session) == 0):
        return redirect("/")
    moneyToSend = int(request.form['money'])
    userForMoney = request.form['user'] + session['uuid']
    query = "select * from users where username = ?;"
    conn = sqlite3.connect('file:data.sqlite?mode=ro', uri=True)
    cursor = conn.cursor()
    cursor.execute(query,(session['username']+session['uuid'],))
    r = cursor.fetchall()
    if(r[0][3] > moneyToSend and moneyToSend > 0):
        time.sleep(10)
        resp = execReadQuery("select money from users where username = ?",(userForMoney,))
        if(len(resp) == 0 ):
          msg = "user doesn't exist"
        else:
          money = resp[0][0]
          execWriteQuery("update users set money= ? where username= ?;", (money + moneyToSend,userForMoney))
          execWriteQuery("update users set money= ? where username= ?;", (r[0][3] - moneyToSend,session['username'] + session['uuid']))
          msg = "successfully sent money"
          resp = execReadQuery("select money from users where username = ?",(session['username'] + session['uuid'],))
          session['money'] = resp[0][0]
    else:
        msg = "not enough balance"
    return render_template("sendMoney.html",msg=msg,money=session['money'])


  elif(request.method == "GET"):
    if(len(session) == 0):
        return redirect("/")
    else:
        return render_template("sendMoney.html",money=session['money'],msg="")

@app.route("/logout")
def logout():
    session['incorrect'] = 0
    session['username'] = ""
    session['money'] = 0
    session['fetchimg'] = "/static/banker.gif"
    return redirect("/")
    

@app.route("/login", methods=["POST","GET"])
def login():
    if(len(session) == 0):
        return redirect("/")
    
    conn = sqlite3.connect('data.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users WHERE username=?;",('broke'+session['uuid'],))
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.execute("INSERT INTO users(username,password,money) VALUES ('broke" + session['uuid'] + "', 'IamBroke', 1000),('useless_fellow" + session['uuid'] + "', 'IamBrokeAgain', 1000);")        
    conn.commit()
    conn.close()

    if(session['incorrect'] > 3):
        return render_template("hacker.html")
    if request.method == "POST":
        username = request.form['username'] + session['uuid']
        passwd = request.form['passwd']
        conn = sqlite3.connect('data.sqlite')
        cursor = conn.cursor()
        query = "select * from users where username = ? AND password = ? ;"
        conn = sqlite3.connect('file:data.sqlite?mode=ro', uri=True)
        cursor = conn.cursor()
        cursor.execute(query, (username, passwd))
        r = cursor.fetchall()
        print(r)
        if len(r) == 1 and r[0][1] == username and r[0][2] == passwd:
            session['username'] = username[:-32]
            session['money'] = r[0][3]
            return redirect("/")
        else:
            session['incorrect'] += 1
            if len(r) == 1:
                return render_template("login.html", message = "unsuccessful login")
            return render_template("login.html", message = "incorrect username or password")
    return render_template("login.html", message="")

if __name__ == '__main__':
    app.run(debug=False)
