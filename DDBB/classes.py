import sqlite3
conect = sqlite3.connect("BUSSI")
cursor = conect.cursor()
from tabulate import tabulate
# cursor.execute("CREATE TABLE INVENT(ID integer primary key AUTOINCREMENT UNIQUE , NAME VARCHAR(50), PRICE INTEGER, CANT INTEGER)")
class ops:

    def login(user, passw):
        if(user == "Admin" and passw == "123"):
            return True
        else:
            return False

    def add(Id,name, priceU, cant):
        new_product = [(name, priceU, cant)]
        cursor.executemany("INSERT INTO INVENT VALUES(NULL,?,?,?)", new_product)
        conect.commit()
        print("-"*30 + " "*10 + "Successfully" + " "*10 + "-"*30 )
    def search(Id):
        cursor.execute("SELECT * FROM INVENT WHERE ID={0}".format(Id))
        data = cursor.fetchone()
        table = [[data[0], data[1], data[2], data[3]]]
        print(tabulate(table, headers=["ID", "Name", "Preci", "Cant"]))