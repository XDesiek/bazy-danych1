import psycopg2
from sqlcreate import createacc,createcars, createclient, createrent
try:
        connection = psycopg2.connect(user="postgres",
                                        password="123",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="car_rent2")
        cursor = connection.cursor()
        cursor.execute(createacc())
        connection.commit()
        cursor.execute(createcars())
        connection.commit()
        cursor.execute(createclient())
        connection.commit()
        cursor.execute(createrent())
        connection.commit()
        dele=input("do u want to delete? y/n")
        while dele=='y':
            tabletodelete=input("wich one?\naccuonts\ncars\nclient\nrent\nall\n")
            if tabletodelete== 'all':
                cursor.execute(f"DROP TABLE accounts;")
                connection.commit()
                cursor.execute(f"DROP TABLE cars;")
                connection.commit()
                cursor.execute(f"DROP TABLE client;")
                connection.commit()
                cursor.execute(f"DROP TABLE rent;")
                connection.commit()            
            else:
                cursor.execute(f"DROP TABLE {tabletodelete};")
                connection.commit()
                dele=input("do u want to delete next table? y/n\n")
except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")