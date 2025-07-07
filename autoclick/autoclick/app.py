#clicker 
from flask import Flask, render_template, request,session,redirect,send_file, make_response
import time
from random import random

import uuid
app = Flask(__name__)
app.secret_key = str(uuid.uuid4())

@app.route('/')
def clicker():
    print(request.form)
    if(len(session) == 0 or 'time' not in request.cookies):
      session['clicks'] = 0
      resp = make_response("<h1><button><a href='/clicked'>click me 1000 times for flag (" + str(session['clicks']) + ")</a></button></h1> <!-- learn about python requests -> https://www.youtube.com/watch?v=tb8gHvYlCFs https://www.geeksforgeeks.org/session-objects-python-requests/ -->")
      print(time.time())
      resp.set_cookie("time",str(int(time.time())))
      return resp
    return "<h1><button><a href='/clicked'>click me 1000 times for flag (" + str(session['clicks']) + ")</a></button></h1>"

@app.route('/clicked')
def clicked():
    if(len(session) == 0 or 'time' not in request.cookies or 'clicks' not in session):
      return redirect('/')
    if(session['clicks'] > 0 and session['clicks'] % 5 == 0 and int(int(request.cookies['time']) / 1000) == int(time.time() / 1000)):
      return "you have done enough clicks for the day, come back tomorrow"
    elif(session['clicks'] > 0 and session['clicks'] % 5 == 0 and int(int(request.cookies['time']) / 1000) != int(time.time() / 1000)):
       session['clicks'] += 1
       resp = redirect('/')
       resp.set_cookie('time',str(int(time.time())))
       return resp
    session['clicks'] += 1
    if(session['clicks'] > 500 and request.headers.get('User-Agent') != "nice_browser"):
       return ("as you have become one of the elite clickers of the world, you need to use 'nice_browser' to keep clicking (it is part of our business strategy)")
    if(session['clicks'] > 1000):
       return("here is the flag - bi0sblr{d1d_y0u_lik3_d0ing_5_cl1cks_3veryd4y?}<br>")
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
