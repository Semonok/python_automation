import mysql.connector
from model.group import Group
from model.contact import Contact


class Dbfixture:

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=database, user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self):
        arr = []
        cursor = self.connection.cursor()
        cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
        for row in cursor.fetchall():
            arr.append(Group(id=str(row[0]), name=row[1], header=row[2], footer=row[3])) # это индексы id,name,header,footer)
        return arr

    def get_contact_list(self):
        arr = []
        cursor = self.connection.cursor()
        cursor.execute('select id, firstname, lastname from addressbook where deprecated = "0000-00-00 00:00:00" ')
        for row in cursor.fetchall():
            arr.append(Contact(id=str(row[0]), firstname=row[1], lastname=row[2]))  # это индексы id,name,header,footer)
        return arr





    def destroy(self):
        self.connection.close()

