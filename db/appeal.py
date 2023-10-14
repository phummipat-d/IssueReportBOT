from db.dbConfig import *

class AppealInfo:
    def Insert(self,userId,displayName,personName,detail,progress,lon,lat,unit):
        sql = "INSERT INTO appeal_info (userId,displayName,personName,detail,progress,lon,lat,unit) VALUES ('"+str(userId)+"','"+str(displayName)+"','"+str(personName)+"','"+str(detail)+"','"+str(progress)+"',"+str(lon)+","+str(lat)+",'"+str(unit)+"')"
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
            MyDatabse.commit()
        except Exception as e:
            print("Error Message for Inserting : ",str(e))
        return MyCursor.lastrowid

    def Update(self,updateSQL,id):
        sql = "UPDATE appeal_info SET "+str(updateSQL)+" WHERE id = "+str(id)
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
            MyDatabse.commit()

        except Exception as e:
            print("Error Message : ",str(e))

        return id
    
    def Select(self,whereCause=""):
        #print(whereCause)
        if whereCause != "":
            whereCause = " where "+str(whereCause)
        sql = "select id,userId,displayName,personName,detail,progress,lon,lat,unit,DATE_FORMAT(updateDate,'%Y-%m-%d') as updateDate from appeal_info "+str(whereCause)
        sql = sql + " ORDER BY id DESC "

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
    

    def Delete(self,whereCause = "id=0"):
        if whereCause != "":
            whereCause = "where "+str(whereCause)
        sql = "DELETE FROM appeal_info "+str(whereCause)

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
            MyDatabse.commit()

        except Exception as e:
            print("Error Message : ",str(e))

    def InsertImage(self,message_id,path,fid):
        sql = "INSERT INTO images (message_id,path,fid) VALUES ('"+str(message_id)+"','"+str(path)+"','"+str(fid)+"')"
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
            row_id = MyCursor.lastrowid
            MyDatabse.commit()

        except Exception as e:
            print("Error Message : ",str(e))            
        return row_id

    def getColumnNames(self):
        sql = "select id,userId,displayName,personName,detail,progress,lon,lat,unit,DATE_FORMAT(updateDate,'%Y-%m-%d') as updateDate from appeal_info Limit 1 "
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
        return MyCursor
