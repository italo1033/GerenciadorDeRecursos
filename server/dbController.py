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
                print("Recurso Inserido!")

    def updateResource(self, id, resource):
        connection = self.getConnection()
        with connection:
            with connection.cursor() as cursor:
                sql = 'UPDATE resource_file  SET name=%s WHERE id_resource_file=%s'
                cursor.execute(sql,(resource , id))
                connection.commit()
                print("Recurso Atualizado!")
    def deleteResource(self, id):
        connection = self.getConnection()
        with connection:
            with connection.cursor() as cursor:
                sql = 'DELETE FROM resource_file WHERE id_resource_file=%s'
                cursor.execute(sql,(id))
                connection.commit()
                print("Recurso Deletado!")
    
    def deleteUser(self, id):
        connection = self.getConnection()
        with connection:
            with connection.cursor() as cursor:
                sql = """ SELECT idAlocation FROM alocation where userID=%s"""
                cursor.execute(sql,(id))
                result = cursor.fetchall()
                if(result):
                    query= """DELETE FROM alocation  WHERE userID = %s"""
                    cursor.execute(query,(id))
                    connection.commit()
                    sql = """DELETE FROM user WHERE idUser=%s"""
                    cursor.execute(sql,(id))
                    connection.commit()
                    print("Usuario Deleteado!")
                else:
                    sql = """DELETE FROM user WHERE idUser=%s"""
                    cursor.execute(sql,(id))
                    connection.commit()
                    print("Usuario Deleteado!")

    def AlocationResource(self, idResource, idUser, dataInitial, dataFinal):
        connection = self.getConnection()
        with connection:
            with connection.cursor() as cursor:
                sql = 'INSERT INTO alocation (`resource_fileID`,`userID`, `dateIntial`, `dateFinal`) VALUES (%s,%s,%s,%s)'
                cursor.execute(sql,(idResource, idUser, dataInitial, dataFinal))
                connection.commit()
                print("Locação Registrada!")

        
        

