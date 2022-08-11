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
def list_resource():
    return conection.select()


@app.post("/insertResource/{name}")
def add_resource(name):
    conection.insertResource(name)
    return {'message':'sucessful'}

@app.post("/updateResource/{id_resource}&{name}")
def update_resource(name, id_resource:int):
    conection.updateResource(id_resource,name)
    return {'message':'sucessful'}

