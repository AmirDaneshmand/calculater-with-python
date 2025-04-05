import psycopg2

conn = psycopg2.connect(dbname="studentdb", user='postgres', password='123', host='localhost', port='5432')
print(conn)