import psycopg2

connection = psycopg2.connect("postgresql://postgres:dev123@localhost/clases")
cursor = connection.cursor()

#cursor.execute('insert into table2(id,completed) values(1,true)')
#cursor.execute('insert into table2(id,completed) values(%s,%s);',(2,True))
cursor.execute('insert into table2(id,completed) values(%(id)s,%(completed)s);',{'id':3,'completed':False})
connection.commit()
connection.close()
cursor.close()