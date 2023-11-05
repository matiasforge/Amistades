from flask import Flask
import pymysql

app = Flask(__name__)
app.secret_key = 'secreto'

DB_NAME = 'Amistades'
db = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db=DB_NAME,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor,
    autocommit=True
)
