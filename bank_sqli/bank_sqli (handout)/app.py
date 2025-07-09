import sqlite3
from flask import Flask, render_template, request,session,redirect,send_file
import os
import uuid
app = Flask(__name__)

app.secret_key = str(uuid.uuid4())


bquote = "<redacted>"

equote = "<redacted>"

flag = os.environ.get("flag")

message = ""
@app.route("/")
def home():
    print("going home")
    msg=""
    print(len(session))
    if len(session) == 0:
        session['incorrect'] = 0
        session['username'] = ""
        session['money'] = 0
        session['fetchimg'] = "/static/weewoo.gif"
    if(session['username'] == 'admin'):
        return redirect('/admin')
    if session['money'] > 100000000:
        msg = "you are elegible for the ultimate credit card, only for the super rich!"
    else:
        msg = "This is the most secure bank in history, only the one in control of the bank can change the money in everyone's accounts"
        session['fetchimg'] = "/static/weewoo.gif"
    if session['username'] == "":
        money = ""
    else:
        money = "money : " + str(session['money'])
#        
        if session['money'] > 100000000:
            money += flag
#
    return render_template("index.html", user = session['username'] , msg = msg, src=session['fetchimg'], money= money)
files = ["creditcard.jpg","flag.txt","weewoo.gif"]

@app.route("/admin", methods=["GET","POST"])
def admin():
    if request.method == "POST" and session['username'] == "admin":
        user = request.form['username']
        money = request.form['money']
        conn = sqlite3.connect('data.sqlite')
        cursor = conn.cursor()
        cursor.execute("update users set money= ? where username= ?;", (money,user))
        conn.commit()
        conn.close()
        return redirect('/')
    if(len(session) !=0 and session['username'] == 'admin'):
        query= "select * from users"
        conn = sqlite3.connect('file:data.sqlite?mode=ro', uri=True)
        cursor = conn.cursor()
        cursor.execute(query)
        r = cursor.fetchall()
        return render_template("admin.html",r = r)
    print(session)
    return "no admin"

@app.route("/login", methods=["POST","GET"])
def login():
    if(len(session) == 0):
        return redirect("/")
    print(session['incorrect'])
    if(session['incorrect'] > 5):
        return render_template("hacker.html")
    if request.method == "POST":
        username = request.form['username']
        passwd = request.form['passwd']
        session['fetchimg'] = request.form['ad']
        query = "select * from users where username = " + bquote + username + equote + " AND password = " + bquote +  passwd +  equote + ";"
        if "--" in username or "--" in passwd or "/*" in username or "/*" in passwd:
            return render_template("hacker.html")
        print(query)
        conn = sqlite3.connect('file:data.sqlite?mode=ro', uri=True)
        cursor = conn.cursor()
        cursor.execute(query)
        r = cursor.fetchall()
        print(r)
        if len(r) == 1 and r[0][1] == username and r[0][2] == passwd:
            session['username'] = username
            session['money'] = r[0][3]
            return redirect('/')
        else:
            session['incorrect'] += 1
            if len(r) == 1:
                return render_template("login.html", message = "unsuccessful login")
            return render_template("login.html", message = "incorrect username or password")
    return render_template("login.html", message="")

if __name__ == '__main__':
    app.run(debug=False)
