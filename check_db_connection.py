import mysql.connector
from model.group import Group


connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    var = connection.cursor()
    var.execute("select * from group_list")
    for raw in var:
        arr = []
        arr.append(Group(id=str(raw[1]), name=raw[6], header=raw[7], footer=raw[8]))
    print(arr)
finally:
    connection.close()