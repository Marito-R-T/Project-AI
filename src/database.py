import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="coorporacion"
)

write = mysql.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="coorporacion"
)


cursor = db.cursor(buffered=True)

