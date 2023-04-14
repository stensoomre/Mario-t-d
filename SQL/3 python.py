
import sqlite3
import csv

conn = sqlite3.connect('epood_eteppan;')
c = conn.cursor()


functions = []


def query_1():
    # Kuva read, kus on vanemad autod, kui 2000 aasta, sorteeri aasta järgi tõusvas järjekorras
    c.execute("SELECT * FROM eteppan WHERE car_year > 2000 ORDER BY car_year ASC")
    rows = c.fetchall()
    for row in rows:
        print(row)


def query_2():

    c.execute("SELECT AVG(car_year), MAX(car_price) FROM eteppan")
    row = c.fetchone()
    print("Keskmine autode aasta: {}, kõige kallim hind: {}".format(row[0], row[1]))


def query_3():
 
    c.execute("SELECT car_make, car_model FROM eteppan ORDER BY car_year DESC LIMIT 5")
    rows = c.fetchall()
    for row in rows:
        print(row)


def query_4():
  
    mark = input("Sisesta automark: ")
    c.execute("SELECT * FROM eteppan WHERE car_make=? ORDER BY car_price DESC LIMIT 5", (mark,))
    rows = c.fetchall()
    for row in rows:
        print(row)


def query_5():
   
    mark = input("Sisesta automark: ")
    c.execute("DELETE FROM eteppan WHERE car_year < 2000 AND car_make=?", (mark,))
    conn.commit()
    print("{} kirjet kustutati".format(c.rowcount))


def query_6():
    
    with open('autod.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        c.execute("SELECT * FROM eteppan")
        rows = c.fetchall()
        for row in rows:
            writer.writerow(row)
    print("Andmed eksporditud faili 'autod.csv'")


def query_7():
    
    c.execute("DELETE FROM eteppan")
    conn.commit()
    print("{} kirjet kustutati".format(c.rowcount))



functions.append(query_1)
functions.append(query_2)
functions.append(query_3)
functions.append(query_4)
functions.append(query_5)
functions.append(query_6)
functions.append(query_7)




def menu():
    while True:
        print("Vali funktsioon:")
        for i in range(len(functions)):
            print("{}. {}".format(i+1, functions[i].__name__))
        print("{}. Välju".format(len(functions)+1))
        choice = input("Sisesta valik (1-{}): ".format(len(functions)+1))
        if choice.isdigit() and int(choice) in range(1, len(functions)+2):
            choice = int(choice)
        if choice == len(functions)+1:
            print("Väljun programmist")
            break
        else:
            func = functions[choice-1]
            func();

