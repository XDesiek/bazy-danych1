import psycopg2
try:
    connection = psycopg2.connect(user="postgres",
                                    password="123",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="dvdrental")
    cursor = connection.cursor()
    cursor.execute("SELECT * from actor")
    records = cursor.fetchall()
    for record in records:
        print(record)
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

delete_query = """Delete from mobile where id = 1"""
    cursor.execute(delete_query)
    connection.commit()
    