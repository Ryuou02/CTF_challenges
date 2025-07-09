import sqlite3
from flask import Flask, render_template, request,session,redirect,send_file
import time
import os
import uuid
app = Flask(__name__)

app.secret_key = str(uuid.uuid4())

flag = "flag{test_flag}"

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
    r = cursor.fetchall()
    conn.commit()
    conn.close()
    

message = ""
@app.route("/")
def home():
    msg=""
    print(len(session))
    if len(session) == 0:
        session['incorrect'] = 0
        session['username'] = ""
        session['money'] = 0
        session['fetchimg'] = "/static/banker.gif"
    if(session['username'] == 'admin'):
        return redirect('/admin')
    else:
        msg = "This is the most secure bank in history, only the one in control of the bank can change the money in everyone's accounts"
        session['fetchimg'] = "/static/banker.png"
    if session['username'] == "":
        money = ""
    else:
        money = str(session['money'])
        if session['money'] > 10000:
            msg=money
    return render_template("index2.html", user = session['username'] , msg = msg)


@app.route("/send-money", methods=["POST","GET"])
def sendMoney():
  if(request.method == "POST"):
    if(len(session) == 0):
        return redirect("/")
    moneyToSend = int(request.form['money'])
    userForMoney = request.form['user']
    query = "select * from users where username = ?;"
    conn = sqlite3.connect('file:data.sqlite?mode=ro', uri=True)
    cursor = conn.cursor()
    cursor.execute(query,(session['username'],))
    r = cursor.fetchall()
    
    if(r[0][3] > moneyToSend and moneyToSend > 0):
        time.sleep(5)
        resp = execReadQuery("select money from users where username = ?",(userForMoney,))
        if(len(resp) == 0 ):
          msg = "user doesn't exist"
        else:
          money = resp[0][0]
          execWriteQuery("update users set money= ? where username= ?;", (money + moneyToSend,userForMoney))
          execWriteQuery("update users set money= ? where username= ?;", (r[0][3] - moneyToSend,session['username']))
          msg = "successfully sent money"
          resp = execReadQuery("select money from users where username = ?",(session['username'],))
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
    if(session['incorrect'] > 3):
        return render_template("hacker.html")
    if request.method == "POST":
        username = request.form['username']
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
            session['username'] = username
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
