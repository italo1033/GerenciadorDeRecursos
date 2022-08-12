import pymysql.cursors

class DbController():
    def getConnection(self):
        connection = pymysql.connect(host='localhost',
                                user='root',
                                password='33!Talo10@',
                                database='resource_menager',
                                cursorclass=pymysql.cursors.DictCursor)
        return connection

    def select(self, userID):
        connection = self.getConnection()
        with connection:
            with connection.cursor() as cursor:
                sql = """   SELECT resource_file.name
                            FROM administrator_has_resource
                            INNER JOIN user ON administrator_has_resource.administratorID = user.administratorID
                            INNER JOIN resource_file ON administrator_has_resource.resource_fileID = resource_file.id_resource_file 
                            where idUser=%s """
                cursor.execute(sql, (userID))
                result = cursor.fetchall()
                return result

    def insertResource(self, resource):
        connection = self.getConnection()
        with connection:
            with connection.cursor() as cursor:
                sql = 'INSERT INTO resource_file (`name`) VALUES (%s)'
                cursor.execute(sql,(resource))
                connection.commit() #Confirmado Insert
                

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

        
        

