from GerenciadorDeRecursos.database.crud.dbController import DbController
from fastapi import FastAPI

conection = DbController()
# # 
# # conection.insertResource("Azul")
# # conection.updateResource(19,"verde")
# # conection.deleteResource(19)
# # conection.deleteUser(2)
# conection.AlocationResource(5,3,"2022-05-05", "2022-06-06" )


app = FastAPI()


@app.get("/listResource/{userID}")
def list_resource(id:int):
    return conection.select(id)


@app.post("/insertResource/{name}&{id_resource}&{id_administrator}")
def add_resource(id_resource:int, name, id_administrator:int ):
    conection.insertResource(id_resource, name, id_administrator)
    return {'message':'sucessful'}

@app.post("/AlocationResource/{id_resource}&{id_user}&{dateInitial}&{FinalInitial}")
def alocation_Resource(id_resource:int, id_user:int , dateInitial,FinalInitial  ):
    conection.AlocationResource(id_resource,id_user,dateInitial, FinalInitial)
    return {'message':'sucessful'}

@app.put("/updateResource/{id_resource}&{name}")
def update_resource(name, id_resource:int):
    conection.updateResource(id_resource,name)
    return {'message':'sucessful'}

@app.delete("/deleteResource/{id}")
def delete_resource(id:int):
    conection.deleteResource(id)
    return {'message':'sucessful'}

@app.delete("/deleteUser/{id}")
def delete_user(id:int):
    conection.deleteUser(id)
    return {'message':'sucessful'}



