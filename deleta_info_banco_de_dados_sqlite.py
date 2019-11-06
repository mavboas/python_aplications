'''
Autor: Marcelo Vilas Boas
data: 23/10/2019 as 9:31 am
requerimentos: sqlite3
'''

import sqlite3

def deleteRecord(path, statement,tabela,coluna):
    try:
        sqliteConnection = sqlite3.connect(path)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        # Deleting single record now
        sql_delete_query = """DELETE from {0} where {1} = '{2}'""".format(tabela,coluna,statement)
        print(sql_delete_query)
        cursor.execute(sql_delete_query)
        sqliteConnection.commit()
        print("Record deleted successfully ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete record from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("the sqlite connection is closed")


