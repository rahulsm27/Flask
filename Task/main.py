import mysql.connector as conn
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/sql', methods = ['GET','POST'])
def fetchsql():
    mydb = conn.connect(host='localhost', user='root')
    cursor = mydb.cursor()
    cursor.execute("select * from cardataset.car")
    x = cursor.fetchall()
    return (jsonify(x))
