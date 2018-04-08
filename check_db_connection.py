import mysql.connector
from fixture.orm import ORMFixture
from model.group import Group


#def check_contact_in_group():
db = ORMFixture(host="127.0.0.1", database="addressbook", user="root", password="")
massive = []
try:
    L = db.get_contacts_in_group(Group(id='165'))
    for i in L:
        massive.append(i)
    print(massive)
    print(len(L))
finally:
   pass #db.destroy()