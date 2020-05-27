import sqlite3

def connection():
  conn = sqlite3.connect('./db/main.db')
  
  print "\n---\nDatabase connected"

  return conn