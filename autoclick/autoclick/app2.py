from flask import Flask, render_template, request,session,redirect,send_file, make_response
import uuid
from random import random

app = Flask(__name__)
app.secret_key = str(uuid.uuid4())

@app.get('/maths')
def mafs():
   if 'a' not in session or 'b' not in session:
      a = int(random() * 10)
      b = int(random() * 10)
      return(f'{str(a)} + {str(b)}') 
   if 'answer' in request:
      if request['answer'] == a + b:
         if 'correct' in session:
            session['correct'] += 1
         else:
            session['correct'] = 1
      else:
         session['correct'] = 0

if __name__ == '__main__':
  app.run(debug=True)