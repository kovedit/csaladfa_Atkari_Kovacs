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
    print(h)

#funkció
def Kereses(id):
    cursor.execute(f"select vezeteknev, keresztnev from ember where id = {id}")
    eredmeny = cursor.fetchall()
    return eredmeny"""

be = input("Írjon be egy vezetéknevet: ")
be2 = input("Írjon be egy keresztnevet: ")

#összes adata
cursor.execute(f"SELECT * FROM `ember` WHERE vezeteknev like '{be}%' AND keresztnev like '{be2}%' ")
keresett = cursor.fetchone()


print(f"Születés helye, ideje: {keresett[3]}, {keresett[4]}")
print(f"Foglalkozása: {keresett[5]}")
print(f"Halálozási helye, ideje, oka: {keresett[9]}, {keresett[7]} - {keresett[8]}")


#neme
cursor.execute(f"select nem from `ember` where vezeteknev like '{be}%' AND keresztnev like '{be2}%' ")
neme1 = cursor.fetchone()
neme = neme1[0]
print(f"Neme: {neme}")

#id-ja
cursor.execute(f"Select id from `ember` where vezeteknev like '{be}%' AND keresztnev like '{be2}%' ")
id1 = cursor.fetchone()
id = id1[0]


#gyerekei
cursor.execute(f"select vezeteknev from `ember` where anyja_id = '{id}' or apja_id = '{id}' ")
vezeteknevek = cursor.fetchall()

cursor.execute(f"select keresztnev from `ember` where anyja_id = '{id}' or apja_id = '{id}' ")
keresztnevek = cursor.fetchall()

(list(zip(vezeteknevek, keresztnevek)))

print("Gyerekei:")
for vezeteknev, keresztnev in zip(vezeteknevek, keresztnevek):
    print(f"\t{vezeteknev[0]} {keresztnev[0]}")


#férje/felesége
if (neme == "nő"):
    cursor.execute(f"select ferj_id from hazas where feleseg_id = '{id}'")
    ferj_id = cursor.fetchone()
    if (len(ferj_id) == 0):
        print("Nincs férje")
    else:
        cursor.execute(f"select vezeteknev, keresztnev from ember where id = {ferj_id[0]}")
        ferj_nev = cursor.fetchone()
        print(f"A férje neve: {ferj_nev[0]} {ferj_nev[1]}")
        cursor.execute(f"select hazassag_ido, hazassag_hely from hazas where feleseg_id = {ferj_id[0]}")
        hazassag = cursor.fetchone()
        print(f"Házasság helye, ideje: {hazassag[1]}, {hazassag[0]}")
else:
    cursor.execute(f"select feleseg_id from hazas where ferj_id = '{id}'")
    feleseg_id = cursor.fetchone()
    if (len(feleseg_id) == 0):
        print("Nincs felesége")
    else:
        cursor.execute(f"select vezeteknev, keresztnev from ember where id = {feleseg_id[0]}")
        feleseg_nev = cursor.fetchone()
        print(f"A felesége neve: {feleseg_nev[0]} {feleseg_nev[1]}")

        cursor.execute(f"select hazassag_ido, hazassag_hely from hazas where feleseg_id = {feleseg_id[0]}")
        hazassag = cursor.fetchone()
        print(f"Házasság helye, ideje: {hazassag[1]}, {hazassag[0]}")

#anyja, apja
cursor.execute(f"select anyja_id, apja_id from ember where id = '{id}'")
van_e = cursor.fetchone()

if (van_e[0] == None):
    print("Nincsenek a családfában a szülei")
else:
    anyjaid = van_e[0]
    apjaid = van_e[1]
    cursor.execute(f"select vezeteknev, keresztnev from ember where id = {anyjaid}")
    anyja_neve = cursor.fetchone()
    print(f"Az anyja neve: {anyja_neve[0]} {anyja_neve[1]}")
    cursor.execute(f"select vezeteknev, keresztnev from ember where id = {apjaid}")
    apja_neve = cursor.fetchone()
    print(f"Az apja neve: {apja_neve[0]} {apja_neve[1]}")

