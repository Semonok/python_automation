import mysql.connector
from model.group import Group


class Dbfixture:

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=database, user=user, password=password)

    def get_group_list(self):
        arr = []
        cursor = self.connection.cursor()
        cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
        for row in cursor.fetchall():
            (id, name, header, footer) = row
            arr.append(Group(id=str(id), name=name, header=header, footer=footer)) # это индексы id,name,header,footer)
        return arr




    def destroy(self):
        self.connection.close()

