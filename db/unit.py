from db.dbConfig import *

class Unit():
    def Select(self):
        sql = "select id,Name from unit "
        try:
            import mysql.connector
            MyDatabse = mysql.connector.connect(
                host = mysql_host,
                user = mysql_user,
                password = mysql_password,
                database = mysql_database
                )
            MyCursor = MyDatabse.cursor()

            MyCursor.execute(sql)
            result = MyCursor.fetchall()

        except Exception as e:
            print("Error Message : ",str(e))
        return result