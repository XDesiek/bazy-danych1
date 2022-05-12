import psycopg2


def mainprint():
    records = cursor.fetchall()
    for record in records:  
        print(record)
    print('\n')

databs='dvdrental'
table="actor"
action=input ('what do want to do?\nshowall\nadd\ndelete\nedit\nnothing\n')
while action=='showall'or 'add'or 'delete'or 'edit':



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
            second_name=input('second name?\n')
            cursor.execute(f"INSERT INTO {table}(First_Name, Last_Name) VALUES ('{name}', '{second_name}') returning (First_Name, Last_Name);")
            mainprint()
        
        # elif action=='delete':
        # elif action=='edit':
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    action=input ('what do want to do?\nshowall\nadd\ndelete\nedit\nnothing\n')