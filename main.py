import tkinter as tk
from functools import partial
import requests
import json

from dbConn import connection
from loginController import Login
from userController import User

loginCtrl = Login(connection())
userCtrl  = User(connection())

# create a new table if now exists
loginCtrl.create_table()
userCtrl.create_table()

errorMsg = ""

class LoginWindow:
  def __init__(self, master):
    self.master = master

    self.master.geometry('300x300')
    self.master.title('Login')
    self.frame = tk.Frame(self.master)
    self.w = "300"
    self.h = "2"
    self.errorMsg = ''
    self.is_login()

  def is_login(self):
    credential = userCtrl.list_data()
    if credential == None:
      self.main_wrap()
    elif '_id' in credential and 'token' and credential:
      # if exists crendential open to welcome window
      self.welcome_window()
    else:
      self.main_wrap()

  def main_wrap(self):
    # Form Label
    self.loginTitle = tk.Label(self.frame, text="Login Area", bg="#333333", fg="#ffffff", width=self.w, height=self.h).pack()
    self.loginBr = tk.Label(self.frame, text="").pack(pady=1) # break row
    # Form Input
    ## Username
    self.loginLabelUsername = tk.Label(self.frame, text="Username", width=self.w, height=self.h, anchor=tk.W).pack(padx=20)
    self.username = tk.StringVar()
    self.loginentryUsername = tk.Entry(self.frame, textvariable=self.username, width=self.w).pack(padx=20, pady=1)
    ## Password
    self.loginLabelPassword = tk.Label(self.frame, text="Password", width=self.w, height=self.h, anchor=tk.W).pack(padx=20)
    self.password = tk.StringVar()
    self.loginEntryPassword = tk.Entry(self.frame, textvariable=self.password, show="*", width=self.w).pack(padx=20, pady=1)
    
    self.validateFrom = partial(self.validate_form, self.username, self.password)

    # Login button
    self.loginButtonLogin = tk.Button(self.frame, text="Login", height="2", width="30", command=self.validateFrom).pack(pady=10)
    self.frame.pack()

  def send_form(self, username, password):
    payload = {'username': username, 'password': password}
    
    headers = {'content-type': 'application/json'}
    # connect to nodeJs server with MongoDb
    # https://github.com/albuquerquefabio/nodetomic-api
    r = requests.post('http://localhost:8000/auth/local', data=json.dumps(payload), headers=headers)

    res = json.loads(json.dumps(r.json()))

    # if exists message you got a error
    if 'message' in res: 
      self.errorMsg = '{}'.format(res['message'])
      print self.errorMsg
      # new window
      self.error_window(self.errorMsg)
      return
    else:
      # insert login to make auto connect
      loginCtrl.create(payload)
      # insert user credentials
      userCtrl.create({'_id': res['user']['_id'], 'token': res['token']})

      print res['user']['_id'] # MongoDb create a unique id into _id as default
      print res['token']
      self.welcome_window()
      return

  def validate_form(self, username, password):
    print("Username: ", username.get())
    print("Password: ", password.get())

    if username.get() == '':
      print('Username empty')
      return
    elif password.get() == '':
      print('Password empty')
      return
    else: 
      self.send_form(username.get(), password.get())
      return

  def error_window(self, msg):
    self.errorWindow = tk.Toplevel(self.master)
    self.app = ErrorWindow(self.errorWindow, msg)
  
  def welcome_window(self):
    self.master.destroy()
    self.welcomeWindow = tk.Tk()
    self.app = WelcomeWindow(self.welcomeWindow)


  def close_window(self):
    self.master.destroy()

  def close_db(self):
    loginCtrl.close_connection()
    userCtrl.close_connection()


class ErrorWindow(tk.Frame):
  def __init__(self, master, msg):
    print msg
    self.master = master

    self.master.geometry('300x200')
    self.master.title('Error')
    self.frame = tk.Frame(self.master)
   
    self.w = "300"
    self.h = "2"
    self.errorMsg = msg

    self.errorTitle = tk.Label(self.frame, text="Error", bg="red", fg="#ffffff", width=self.w, height=self.h).pack()
    self.errorBr = tk.Label(self.frame, text="").pack(pady=1) # break row
    self.labelError = tk.Label(self.frame, text="{}".format(self.errorMsg), width=self.w, height=self.h, fg="red").pack(padx=20, pady=20)
    self.button = tk.Button(self.frame, text="OK", height=self.h, width="30", command=self.close_window).pack(pady=10)

    self.frame.pack()
  
  def close_window(self):
    self.master.destroy()

class WelcomeWindow(tk.Frame):
  def __init__(self, master):
    self.master = master

    self.master.geometry('300x200')
    self.master.title('Welcome')
    self.frame = tk.Frame(self.master)
   
    self.w = "300"
    self.h = "2"

    self.windowTitle = tk.Label(self.frame, text="Welcome", bg="#2A3E4C", fg="#ffffff", width=self.w, height=self.h).pack()

    self.logout = tk.Button(self.frame, text="Logout", bg="red", fg="white", height=self.h, width="30", command=self.logout_action).pack(pady=10)

    self.frame.pack()

  def logout_action(self):
    loginCtrl.delete_data()
    userCtrl.delete_data()
    self.close_window()
  
  def close_window(self):
    self.master.destroy()

def main():
  root = tk.Tk()
  app = LoginWindow(root)
  root.mainloop()

if __name__ == '__main__':
  main()