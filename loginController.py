import json
# from dbConn import connection

class Login:
  def __init__(self, conn):
    '''
      Login class

      :param def conn: The conn expected a connection from dbConn

      :return: Connection: db connection
    '''
    self.conn = conn

  def create_table(self):
    '''
      Create a new table LOGIN if not exists

      :return: void
    '''
    self.conn.execute('''CREATE TABLE IF NOT EXISTS LOGIN
              (ID        INTEGER   PRIMARY KEY   AUTOINCREMENT,
              USERNAME   TEXT                    NOT NULL,
              PASSWORD   TEXT                    NOT NULL);''')
    # print "Table created\n---\n"

    self.conn.close()

  def create(self, data):
    '''
      Create a new row into LOGIN 
      :param dict data: User crendentials should be { 'username': str, 'password': str}

      :return: bool
    '''
    obj = json.loads(json.dumps(data))
    if 'username' in obj and 'password' in obj:
      query = "INSERT INTO LOGIN (USERNAME, PASSWORD) \
        VALUES('{}','{}')".format(obj['username'],obj['PASSWORD'])

      self.conn.execute(query)
      self.conn.commit()
      self.conn.close()
      return True
    else:
      return False

  def list_data(self):
    '''
      Show data from db

      :return: dict: {\"id\": str, \"username\": str, \"password\": str}
    '''
    query = "SELECT * FROM LOGIN"
    login = self.conn.execute(query)
    for row in login:
      loginObj = {"id": row[0], "username": row[1], "password": row[2]}
      self.conn.close()
      return loginObj

  def update_data(self, sqlSet, sqlWhere):
    '''
      Update data
      :param str sqlSet: Should be \"sql_field = \'str_value\' \" or \"sql_field1 = \'str_value1\', sql_field2 = \'str_value2\', ... \"
      :param str sqlWhere: Should be \"sql_field = \'str_value\' \" or \"sql_field1 = \'str_value1\', sql_field2 = \'str_value2\', ... \"

      :return: void
    '''
    query = "UPDATE LOGIN set {} WHERE {}".format(sqlSet, sqlWhere)
    self.conn.execute(query)
    self.conn.commit()
    self.conn.close()

  def delete_data(self, sqlWhere = None):
    '''
      Delete data

      :param str or none sqlWhere: Should be \"sql_field = \'str_value\' \" or \"sql_field1 = \'str_value1\', sql_field2 = \'str_value2\', ... \"
      
      if sqlWhere == none it will execute \"DELETE FROM LOGIN\" -> Delete all from LOGIN (PAY ATTENTION)

      :return: void
    '''
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
# create(connection(), {'username': 'someusername', 'password': 'random password goes here'})

# Return a row as python object
# print list_data(connection())

# Update data
# update_data(connection(), "password = '467a7f56-9ff6-11ea-bb37-0242ac130002'", "username = 'someusername'")

# Delete row
# delete_data(connection(), "username = 'someusername'")




