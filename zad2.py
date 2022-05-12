import psycopg2


def mainprint():
    records = cursor.fetchall()
    for record in records:  
        print(record)
    print('\n')

databs='dvdrental'
table="actor"
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
            cursor.execute(f"INSERT INTO {table}(First_Name, Last_Name) VALUES ('{name}', '{last_name}') returning (First_Name, Last_Name);")
            connection.commit()
            mainprint()
        elif action=='delete':
            dlast_name=input('last name to delete?\n')
            cursor.execute(f"DELETE FROM {table} WHERE last_name ='{dlast_name}' returning*;")
            connection.commit()
        elif action=='edit':
            edname=input('name?\n')
            edlast_name=input('last name?\n')
            ename=input('edited name?\n')
            elast_name=input('edited last name?\n')
            cursor.execute(f"UPDATE {table} SET first_name = ename,last_name = 'elast_name' WHERE first_name='{edname}',last_name ='{edlast_name}' returning *;")
            connection.commit()
            mainprint()
except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")