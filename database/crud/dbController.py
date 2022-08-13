import pymysql.cursors

class DbController():
    def getConnection(self):
        connection = pymysql.connect(host='localhost',
                                user='root',
                                password='12',
                                database='resource_menager',
                                cursorclass=pymysql.cursors.DictCursor)
        return connection

    def select(self, userID):
        try:
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
        except Exception as e: 
            return {"message": e}


    def insertResource(self, id_resource, resource, id_administrator):
        try:
            connection = self.getConnection()
            with connection:
                with connection.cursor() as cursor:
                    sql = 'INSERT INTO resource_file (`id_resource_file`,`name`) VALUES (%s,%s)'
                    cursor.execute(sql,(id_resource,resource))
                    connection.commit() #Confirmado Insert

                    query = 'INSERT INTO administrator_has_resource (`administratorID`, `resource_fileID`) VALUES (1,1);'
                    cursor.execute(query,(id_administrator,id_resource))
                    connection.commit() #Confirmado Insert
        except Exception as e: 
            return {"message": e}
                

    def updateResource(self, id, resource):
        try:
            connection = self.getConnection()
            with connection:
                with connection.cursor() as cursor:
                    sql = 'UPDATE resource_file  SET name=%s WHERE id_resource_file=%s'
                    cursor.execute(sql,(resource , id))
                    connection.commit()
                    print("Recurso Atualizado!")
        except Exception as e: 
            return {"message": e}
        
    def deleteResource(self, id):
        try:
            connection = self.getConnection()
            with connection:
                with connection.cursor() as cursor:
                    sql = 'DELETE FROM resource_file WHERE id_resource_file=%s'
                    cursor.execute(sql,(id))
                    connection.commit()
                    print("Recurso Deletado!")
        except Exception as e: 
            return {"message": e}

    def deleteUser(self, id):
        try:
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
        except Exception as e: 
            return {"message": e}

    def AlocationResource(self, idResource, idUser, dataInitial, dataFinal):
        try:
            connection = self.getConnection()
            with connection:
                with connection.cursor() as cursor:
                    sql = 'INSERT INTO alocation (`resource_fileID`,`userID`, `dateIntial`, `dateFinal`) VALUES (%s,%s,%s,%s)'
                    cursor.execute(sql,(idResource, idUser, dataInitial, dataFinal))
                    connection.commit()
                    print("Locação Registrada!")
        except Exception as e: 
            return {"message": e}
        
    def addUser(self, name, id):
        try:
            connection = self.getConnection()
            with connection:
                with connection.cursor() as cursor:
                    sql = 'INSERT INTO user (`name`, `administratorID`) VALUES (%s, %s);'
                    cursor.execute(sql,(name , id))
                    connection.commit()
                    print("Usuario Cadastrado!")
        except Exception as e: 
            return {"message": e}

    def addAdministrator(self, name):
        try:
            connection = self.getConnection()
            with connection:
                with connection.cursor() as cursor:
                    sql = 'INSERT INTO administrator (`name`) VALUES (%s)'
                    cursor.execute(sql,(name))
                    connection.commit()
                    print("Usuario Cadastrado!")
        except Exception as e: 
            return {"message": e}
    
    def deleteAlocation(self, id):
        try:
            connection = self.getConnection()
            with connection:
                with connection.cursor() as cursor:
                    query= """DELETE FROM alocation  WHERE idAlocation = %s"""
                    cursor.execute(query,(id))
                    connection.commit()
                    print("Locacão cancelada")
        except Exception as e: 
            return {"message": e}

    
    def listAdministrator(self):
        try:
            connection = self.getConnection()
            with connection:
                with connection.cursor() as cursor:
                    sql = ' SELECT * FROM  administrator'
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    return result
        except Exception as e: 
            return {"message": e}
    
    def listUser(self,id_administrator):
        try:
            connection = self.getConnection()
            with connection:
                with connection.cursor() as cursor:
                    sql = """
                            SELECT *
                            FROM user
                            INNER JOIN administrator ON administrator.idAdministrator = user.administratorID
                            where administratorID=%s;
                           """
                    cursor.execute(sql,id_administrator)
                    result = cursor.fetchall()
                    return result
        except Exception as e: 
            return {"message": e}



        
        

