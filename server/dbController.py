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
                # Read a single record
                sql = "SELECT * FROM `administrator`"
                cursor.execute(sql)
                result = cursor.fetchall()
                print(result)