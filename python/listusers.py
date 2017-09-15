import mysql.connector
from ConfigParser import ConfigParser

config = ConfigParser()
config.read('.mysql.ini')

cnx = mysql.connector.connect(
  host=config.get('dbatools', 'hostname'),
  user=config.get('dbatools', 'username'),
  password=config.get('dbatools', 'password'),
  database=config.get('dbatools', 'database'))

cursor = cnx.cursor()

query = ('SELECT User, Host FROM mysql.user')

cursor.execute(query)

for (user, host) in cursor:
    print "{}@{}".format(user, host)

cursor.close()
cnx.close()
