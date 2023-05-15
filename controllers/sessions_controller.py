from flask import render_template, request, redirect, session, url_for
from models.user import find_user_by_email

import bcrypt

def new():
  return render_template('sessions/new.html')

def create():
  email = request.form.get('email')
  password = request.form.get('password')
  user = find_user_by_email(email)
  if user == None:
    return redirect('/sessions/new')
  
  valid_password = bcrypt.checkpw(password.encode(), user['password_digest'].encode())
  if valid_password:
    session['user_id'] = user['user_id'] # logs the user in
    return redirect('/')
  else:
    return redirect('/sessions/new')

def delete():
  session.clear() # logs the user out
  return redirect('/')

