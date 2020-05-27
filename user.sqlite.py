import sqlite3
import json

def connection():
  conn = sqlite3.connect('./db/user.db')
  
  print "\n---\nDatabase connected"

  return conn

def create_table(conn):
  conn.execute('''CREATE TABLE IF NOT EXISTS USER
          (ID   INTEGER   PRIMARY KEY  AUTOINCREMENT,
          _ID   TEXT                    NOT NULL,
          TOKEN TEXT                    NOT NULL);''')
  print "Table created\n---\n"

  conn.close()

def create(conn, data):
  obj = json.loads(json.dumps(data))
  if '_id' in obj and 'token' in obj:
    query = "INSERT INTO USER (_ID, TOKEN) \
      VALUES('{}','{}')".format(obj['_id'],obj['token'])

    conn.execute(query)
    conn.commit()
    conn.close()
    return True
  else:
    return False

def list_data(conn):
  query = "SELECT * FROM USER"
  user = conn.execute(query)
  for row in user:
    userObj = {"id": row[0], "_id": row[1], "token": row[2]}
    conn.close()
    return userObj

def update_data(conn, sqlSet, sqlWhere):
  query = "UPDATE USER set {} WHERE {}".format(sqlSet, sqlWhere)
  conn.execute(query)
  conn.commit()
  conn.close()

def delete_data(conn, sqlWhere = None):
  query = "DELETE FROM USER"
  if sqlWhere:
    query = query + " WHERE {}".format(sqlWhere)

  conn.execute(query)
  conn.commit()
  conn.close()



# conn = connection()

# Run create table once
# create_table(connection())


# CRUD - Create Read Update and Delete

# Create a new row
# create(connection(), {'_id': 'some_ID', 'token': 'random token goes here'})

# Return a row as python object
# print list_data(connection())

# Update data
# update_data(connection(), "token = '467a7f56-9ff6-11ea-bb37-0242ac130002'", "_ID = 'some_ID'")

# Delete row
# delete_data(connection(), "_ID = 'some_ID'")




