import psycopg2
from sqlfunctions import add,delete,edit

def mainprint():
    records = cursor.fetchall()
    for record in records:  
        print(record)
    print('\n')

databs='Firma'
table="worker"
action=input ('what do want to do?\nshowall\nadd\ndelete\nedit\nnothing\n')



try:
        connection = psycopg2.connect(user="postgres",
                                        password="123",
                                        host="127.0.0.1",
                                        port="5432",
                                        database=databs)
        cursor = connection.cursor()
        if action=='showall':
            cursor.execute(f"SELECT * from {table}")
            mainprint()
        elif action=='add':
            name=input('name?\n')
            last_name=input('last name?\n')
            print(last_name)
            cursor.execute(add(table,name,last_name))
            connection.commit()
            mainprint()
        elif action=='delete':
            did=input('id to delete?\n')
            cursor.execute(delete(table,did))
            connection.commit()
        elif action=='edit':
            edid=input("Who do you want to edit ( what id )\n")
            edname=input('edited name?\n')
            edlast_name=input('edited last name?\n')
            cursor.execute(edit(table, edname, edlast_name,edid))
            connection.commit()
            mainprint()
except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")