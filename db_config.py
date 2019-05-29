from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'muhammed'
app.config['MYSQL_DATABASE_PASSWORD'] = 'muhammed'
app.config['MYSQL_DATABASE_DB'] = 'muhammed'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
