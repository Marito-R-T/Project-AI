import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="GT"
)

cursor = db.cursor()

