import pyodbc
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=E:\Lorah,Jake\2018-2019\CS4\SQL-Database\Python - Basic Connection\Python_Database.accdb;'
    )
cnxn = pyodbc.connect(conn_str)
cursor = cnxn.cursor()

cursor.execute("Create Table Class (Name char (20), Id Number Primary Key, grade char(3))")
cnxn.commit()
cursor.execute("insert into Class(id,  name, grade) values ('1', 'Math', '95%')")
cnxn.commit()

rows = cursor.execute("select * from Class").fetchall()
if rows:
    print(rows)
