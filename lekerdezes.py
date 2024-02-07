import sqlite3

beolvas = sqlite3.connect("csaladfa.db")

cursor = beolvas.cursor()

"""cursor.execute("SELECT * FROM `ember`")
item = cursor.fetchall()
for i in item:
    print(i)

cursor.execute("SELECT feleseg_id FROM hazas")
hazas = cursor.fetchall()
for h in hazas:
    print(h)"""

#funkció
def Kereses(id):
    cursor.execute(f"select vezeteknev, keresztnev from ember where id = {id}")
    eredmeny = cursor.fetchall()
    return eredmeny

be = input("Írjon be egy vezetéknevet: ")
be2 = input("Írjon be egy keresztnevet: ")

#összes adata
cursor.execute(f"SELECT * FROM `ember` WHERE vezeteknev like '{be}%' AND keresztnev like '{be2}%' ")
keresett = cursor.fetchall()
print(keresett)

#neme
cursor.execute(f"select nem from `ember` where vezeteknev like '{be}%' AND keresztnev like '{be2}%' ")
neme1 = cursor.fetchone()
neme = neme1[0]
print(neme)

#id-ja
cursor.execute(f"Select id from `ember` where vezeteknev like '{be}%' AND keresztnev like '{be2}%' ")
id1 = cursor.fetchone()
id = id1[0]
print(id)

#gyerekei
cursor.execute(f"select * from `ember` where anyja_id = '{id}' or apja_id = '{id}' ")
keresett = cursor.fetchall()
print(keresett)

#férje/felesége
if (neme == "nő"):
    cursor.execute(f"select ferj_id from hazas where feleseg_id = '{id}'")
    ferj_id = cursor.fetchall()
    if (len(ferj_id) == 0):
        print("Nincs férje")
    else:
        cursor.execute(f"select vezeteknev, keresztnev from ember where id = {ferj_id[0]}")
        ferj_nev = cursor.fetchone()
        print(f"A férje neve: {ferj_nev}")
else:
    cursor.execute(f"select feleseg_id from hazas where ferj_id = '{id}'")
    feleseg_id = cursor.fetchall()
    if (len(feleseg_id) == 0):
        print("Nincs felesége")
    else:
        cursor.execute(f"select vezeteknev, keresztnev from ember where id = {feleseg_id[0]}")
        feleseg_nev = cursor.fetchone()
        print(f"A felesége neve: {feleseg_nev}")

#anyja, apja
cursor.execute(f"select anyja_id, apja_id from ember where id = '{id}'")
van_e = cursor.fetchall()
anyjaid = van_e[0]
apjaid = van_e[1]
print(anyjaid)
#if (len(van_e) == 0):
    #print("Nincsenek a családfában a szülei")

