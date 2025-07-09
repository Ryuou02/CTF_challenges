import sqlite3
from flask import Flask, render_template, request,session,redirect,send_file
import os
import uuid
app = Flask(__name__)

app.secret_key = str(uuid.uuid4())
files = ["creditcard.jpg","flag.txt","weewoo.gif"]

bquote = '"'
equote = '"'

def init_db():
    # the database has a table users
    conn = sqlite3.connect('data.sqlite')
    cursor = conn.cursor()
    cursor.execute("delete from users;")    # delete all users from table
    conn.commit()
    conn.close()

message = ""
@app.route("/logout")
def deleteSession():
    session['incorrect'] = 0
    session['username'] = ""
    session['money'] = 0
    session['fetchimg'] = "/static/weewoo.gif"
    return redirect("/")

@app.route("/")
def home():
    print("going home")
    msg=""
    print(len(session))
    if len(session) == 0:
        session["uuid"] = str(uuid.uuid4()).replace('-',"")
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
        money = str(session['money'])
    return render_template("index.html", user = session['username'] , msg = msg, src=session['fetchimg'], money= money)

@app.route("/static/<path>")
def goTo(path):
    try:
        if(session['money'] > 100000000):
            return send_file('/app/static/' + path)
        elif(path != "creditcard.jpg"):
            return send_file('/app/static/' + path)
        else:
            return "you don't have enough money to access the credit card!",403
    except KeyError:
        return redirect('/')
    except FileNotFoundError:
        return "the file doesn't exist",404


@app.route("/admin", methods=["GET","POST"])
def admin():
    if request.method == "POST" and session['username'] == "admin":
        user = request.form['username'] + session['uuid']
        print(user)
        money = request.form['money']
        conn = sqlite3.connect('data.sqlite')
        cursor = conn.cursor()
        cursor.execute("update users set money= ? where username= ?;", (money,user))
        conn.commit()
        conn.close()
        return redirect('/')
    if(len(session) !=0 and session['username'] == 'admin'):
        query= "select * from users where username like '%" + session['uuid'] + "';"
        conn = sqlite3.connect('file:data.sqlite?mode=ro', uri=True)
        cursor = conn.cursor()
        cursor.execute(query)
        r = cursor.fetchall()
        r = [list(row) for row in r]

        for i in range(len(r)):
            r[i][1] = r[i][1][:-32]  # Safely modify username
        return render_template("admin.html",r = r)
    print(session)
    return "no admin",403

@app.route("/register", methods=["POST","GET"])
def reg():
    if(request.method == "GET"):
        return render_template("register.html",message="")
    else:

        username = request.form['username'] + session['uuid']
        passwd = request.form['passwd']
        query = "select * from users where username = ?;"
        conn = sqlite3.connect('data.sqlite')
        cursor = conn.cursor()
        cursor.execute(query,(username,))
        r = cursor.fetchall()

        if(len(r) >= 1):
            return render_template('register.html',message="user already exists")

        query = "insert into users(username,password,money) values( ? , ? ,10);"
        conn = sqlite3.connect('data.sqlite')
        cursor = conn.cursor()
        cursor.execute(query, (username, passwd))
        conn.commit()
        conn.close()
        return redirect('/login')

@app.route("/login", methods=["POST","GET"])
def login():
    if(len(session) == 0):
        return redirect("/")
    
    print(session['incorrect'])
    if(session['incorrect'] > 5):
        return render_template("hacker.html")
    
    conn = sqlite3.connect('data.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users WHERE username=?;",('admin'+session['uuid'],))
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.execute("INSERT INTO users(username,password,money) VALUES ('admin" + session['uuid'] + "', 'AVeryComplexPassword" + session['uuid'] + "', 10);")        
    conn.commit()
    conn.close()

    if request.method == "POST":
        username = request.form['username']
        passwd = request.form['passwd']
        session['fetchimg'] = request.form['ad']
        query = "select * from users where username = ? AND password = " + bquote +  passwd +  equote + ";"
        conn = sqlite3.connect('data.sqlite')
        cursor = conn.cursor()
        cursor.execute(query,(username + session['uuid'],))
        r = cursor.fetchall()
        print(r)
        if len(r) >= 1:
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

#29387989hfksjhNMBOV8W