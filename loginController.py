import json
# from dbConn import connection

class Login:
  def __init__(self, conn):
    self.conn = conn

  def create_table(self):
    self.conn.execute('''CREATE TABLE IF NOT EXISTS LOGIN
              (ID   INTEGER   PRIMARY KEY  AUTOINCREMENT,
              _ID   TEXT                    NOT NULL,
              TOKEN TEXT                    NOT NULL);''')
    # print "Table created\n---\n"

    self.conn.close()

  def create(self, data):
    obj = json.loads(json.dumps(data))
    if '_id' in obj and 'token' in obj:
      query = "INSERT INTO LOGIN (_ID, TOKEN) \
        VALUES('{}','{}')".format(obj['_id'],obj['token'])

      self.conn.execute(query)
      self.conn.commit()
      self.conn.close()
      return True
    else:
      return False

  def list_data(self):
    query = "SELECT * FROM LOGIN"
    login = self.conn.execute(query)
    for row in login:
      loginObj = {"id": row[0], "_id": row[1], "token": row[2]}
      self.conn.close()
      return loginObj

  def update_data(self, sqlSet, sqlWhere):
    query = "UPDATE LOGIN set {} WHERE {}".format(sqlSet, sqlWhere)
    self.conn.execute(query)
    self.conn.commit()
    self.conn.close()

  def delete_data(self, sqlWhere = None):
    query = "DELETE FROM LOGIN"
    if sqlWhere:
      query = query + " WHERE {}".format(sqlWhere)

    self.conn.execute(query)
    self.conn.commit()
    self.conn.close()


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




