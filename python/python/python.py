import sqlite3;

beolvas = sqlite3.connect("csaladfa.db");

cursor = beolvas.cursor();

"""cursor.execute("SELECT * FROM `ember`")
item = cursor.fetchall()
for i in item:
    print(i)

cursor.execute("SELECT feleseg_id FROM hazas")
hazas = cursor.fetchall()
for h in hazas:
    print(h)"""



be = input("Írjon be egy vezetéknevet: ")
be2 = input("Írjon be egy keresztnevet: ")

cursor.execute("SELECT * FROM `ember` WHERE vezeteknev = be AND keresztnev = be2 ")
keresett = cursor.fetchall()
print(keresett)
