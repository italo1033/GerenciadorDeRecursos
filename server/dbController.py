import pymysql.cursors

class DbController():
    def getConnection(self):
        connection = pymysql.connect(host='localhost',
                                user='root',
                                password='33!Talo10@',
                                database='resource_menager',
                                cursorclass=pymysql.cursors.DictCursor)
        return connection

    def select(self):
        connection = self.getConnection()
        with connection:
            with connection.cursor() as cursor:
                sql = """ SELECT * FROM resource_file """
                cursor.execute(sql)
                result = cursor.fetchall()
                print(result)

    def insertResource(self, resource):
        connection = self.getConnection()
        with connection:
            with connection.cursor() as cursor:
                sql = 'INSERT INTO resource_file (`name`) VALUES (%s)'
                cursor.execute(sql,(resource))
                connection.commit() #Confirmado Insert
                print("ok")

    def updateResource(self, id, resource):
        connection = self.getConnection()
        with connection:
            with connection.cursor() as cursor:
                sql = 'UPDATE resource_file  SET name=%s WHERE id_resource_file=%s'
                cursor.execute(sql,(resource , id))
                connection.commit()
                print("ok")
    def deleteResource(self, id):
        connection = self.getConnection()
        with connection:
            with connection.cursor() as cursor:
                sql = 'DELETE FROM resource_file WHERE id_resource_file=%s'
                cursor.execute(sql,(id))
                connection.commit()
                print("ok")
        
        

