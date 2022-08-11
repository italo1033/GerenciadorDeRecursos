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
        
        

