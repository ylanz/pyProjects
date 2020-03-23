from app import app
from flaskext.mysql import MySQL
#from flask_mysqldb.MySQL import MySQL
#from flask.ext.mysql import MySQL

mysql = MySQL()
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = "root"
app.config['MYSQL_DATABASE_PASSWORD'] = ""
app.config['MYSQL_DATABASE_DB'] = "test"
app.config['MYSQL_DATABASE_HOST'] = "localhost"

#mysql = MySQL(app)


mysql.init_app(app)