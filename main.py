from server.dbController import DbController
from fastapi import FastAPI

conection = DbController()
# # 
# # conection.insertResource("Azul")
# # conection.updateResource(19,"verde")
# # conection.deleteResource(19)
# # conection.deleteUser(2)
# conection.AlocationResource(5,3,"2022-05-05", "2022-06-06" )


app = FastAPI()


@app.get("/listResource")
def listResource():
    return conection.select()


@app.post("/insertResource/{name}")
def addResource(name):
    return conection.insertResource(name)