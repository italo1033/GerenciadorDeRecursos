from server.dbController import DbController

conection = DbController()
# conection.select()
# conection.insertResource("Azul")
# conection.updateResource(19,"verde")
# conection.deleteResource(19)
# conection.deleteUser(2)
conection.AlocationResource(5,3,"2022-05-05", "2022-06-06" )