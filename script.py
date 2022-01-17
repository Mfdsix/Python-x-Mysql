import mysql.connector
import json
import collections

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="python_x_mysql"
)

datas = []
cursor = mydb.cursor()
cursor.execute("SELECT * FROM customers")
result = cursor.fetchall()

for row in result:
    d = collections.OrderedDict()
    d["customerNumber"] = row[0]
    d["customerName"] = row[1]
    d["contactLastName"] = row[2]
    d["contactFirstName"] = row[3]
    d["phone"] = row[4]
    d["addressLine1"] = row[5]
    d["city"] = row[6]
    datas.append(d)

print(json.dumps(datas))