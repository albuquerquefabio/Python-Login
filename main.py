from tkinter import *
from functools import partial
import requests
import json

from dbConn import connection
from userController import User
from loginController import Login

userCtrl  = User(connection())
loginCtrl = Login(connection())

userCtrl.create

root = Tk()
root.geometry('300x300')
root.title('Login')


def send_form(username, password):
  payload = {'username': username, 'password': password}
  headers = {'content-type': 'application/json'}
  r = requests.post('http://localhost:8000/auth/local', data=json.dumps(payload), headers=headers)
  res = json.loads(json.dumps(r.json()))

  if 'message' in res: 
    print res['message']
    return
  else:
    print res['token'] 
    return

def validate_form(username, password):
  print("Username: ", username.get())
  print("Password: ", password.get())

  if username.get() == '':
    print('Username empty')
    return
  elif password.get() == '':
    print('Password empty')
    return
  else: 
    send_form(username.get(), password.get())
    return


def main_wrap():

  w = "300"
  h = "2"

  # Form Label
  Label(root, text="Login Area", bg="#333333", fg="#ffffff", width=w, height=h).pack()
  Label(root, text="").pack(pady=1)
  # Form Input
  ## Username
  usernameLabel = Label(root, text="Username", width=w, height=h, anchor=W).pack(padx=20)
  username = StringVar()
  usernameEntry = Entry(root, textvariable=username, width=w).pack(padx=20, pady=1)
  ## Password
  passwordLabel = Label(root, text="Password", width=w, height=h, anchor=W).pack(padx=20)
  password = StringVar()
  passwordEntry = Entry(root, textvariable=password, show="*", width=w).pack(padx=20, pady=1)
  
  validateFrom = partial(validate_form, username, password)

  # Login button
  Button(root, text="Login", height="2", width="30", command=validateFrom).pack(pady=20)


  root.mainloop()

main_wrap()