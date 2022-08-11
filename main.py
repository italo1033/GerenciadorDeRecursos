from server.dbController import DbController

conection = DbController()
# conection.select()
# conection.insertResource("Azul")
conection.updateResource(19,"verde")
