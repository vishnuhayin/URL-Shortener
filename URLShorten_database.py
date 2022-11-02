import sqlite3
import logging

def createTable():
    connection_1 = sqlite3.connect("url_shortner.db")
    cursor_1 = connection_1.cursor()
    try:
        cursor_1.execute("create table user_details(userId int, name text, actualUrl text," +
                         " shortUrl text, creationTime timestamp)")
    except Exception as e:
        logging.exception("exception occured "+ str(e))

    connection_1.commit()
    connection_1.close()

def insertData(table_name, datas):

    query = "insert into " + table_name + " values("

    for i in range(len(datas)):
        try:
            if type(datas[i]) == int:
                query = query + str(datas[i])
            else: query = query + '"' + str(datas[i]) + '"'
        except : continue

        try:
            if datas[i+1]: query += " , "
        except : continue

    query += ");"

    return query

# createTable()