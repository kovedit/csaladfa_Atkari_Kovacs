import sqlite3;

beolvas = sqlite3.connect("csaladfa.db");

cursor = beolvas.cursor();


#with open('csaladfa.sql', 'r') as f:
    #cursor.executescript(f.read())

#vagy

cursor.execute("SELECT * FROM `ember`")
item = cursor.fetchall()
for i in item:
    print(i)