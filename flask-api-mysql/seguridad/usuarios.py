import pymysql
from app import app
from dbConfig import mysql
from flask import jsonify, request


@app.route('/usuarios')
def usuarios():
    try:
        conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM products")
		rows = cursor.fetchall()
		resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
       print(e)
    finally:
        cursor.close() 
		conn.close()

if __name__ == "__main__":
    app.run()
