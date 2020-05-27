import json
# from dbConn import connection

class User:
  def __init__(self, conn):
    '''
      User class

      :param def conn: The conn expected a connection from dbConn

      :return: Connection: db connection
    '''
    self.conn = conn

  def create_table(self):
    '''
      Create a new table USER if not exists

      :return: void
    '''
    self.conn.execute('''CREATE TABLE IF NOT EXISTS USER
              (ID   INTEGER   PRIMARY KEY  AUTOINCREMENT,
              _ID   TEXT                    NOT NULL,
              TOKEN TEXT                    NOT NULL);''')
    # print "Table created\n---\n"

    self.conn.close()

  def create(self, data):
    '''
      Create a new row into USER 
      :param dict data: User crendentials should be { 'username': str, 'password': str}

      :return: bool
    '''
    obj = json.loads(json.dumps(data))
    if '_id' in obj and 'token' in obj:
      query = "INSERT INTO USER (_ID, TOKEN) \
        VALUES('{}','{}')".format(obj['_id'],obj['token'])

      self.conn.execute(query)
      self.conn.commit()
      self.conn.close()
      return True
    else:
      return False

  def list_data(self):
    '''
      Show data from db

      :return: dict: {\"id\": str, \"_id\": str, \"token\": str}
    '''
    query = "SELECT * FROM USER"
    user = self.conn.execute(query)
    for row in user:
      userObj = {"id": row[0], "_id": row[1], "token": row[2]}
      self.conn.close()
      return userObj

  def update_data(self, sqlSet, sqlWhere):
    '''
      Update data
      :param str sqlSet: Should be \"sql_field = \'str_value\' \" or \"sql_field1 = \'str_value1\', sql_field2 = \'str_value2\', ... \"
      :param str sqlWhere: Should be \"sql_field = \'str_value\' \" or \"sql_field1 = \'str_value1\', sql_field2 = \'str_value2\', ... \"

      :return: void
    '''
    query = "UPDATE USER set {} WHERE {}".format(sqlSet, sqlWhere)
    self.conn.execute(query)
    self.conn.commit()
    self.conn.close()

  def delete_data(self, sqlWhere = None):
    '''
      Delete data

      :param str or none sqlWhere: Should be \"sql_field = \'str_value\' \" or \"sql_field1 = \'str_value1\', sql_field2 = \'str_value2\', ... \"
      
      if sqlWhere == none it will execute \"DELETE FROM USER\" -> Delete all from USER (PAY ATTENTION)

      :return: void
    '''
    query = "DELETE FROM USER"
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




