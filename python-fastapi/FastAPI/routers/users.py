from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/user", tags=["user"], responses=({404:{"message" : "No encontrado"}}))

# Entidad User
# ------------
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [
            User(id = 1, name = "David", surname = "Muñoz Fernandez", url = "https://google.com", age = 33),
            User(id = 2, name = "Pepe", surname = "Perez Fernandez", url = "https://google.com", age = 31),
            User(id = 3, name = "Juan", surname = "Gomez Fernandez", url = "https://google.com", age = 35),
        ]

# Obtener
# -------
@router.get("/all")
async def users():
    return users_list

# Path
# ----
@router.get("/{id}")
async def user(id: int):
    return search_user(id)

# Añadir
# ------
@router.post("/add", status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    else:
        users_list.append(user)
        return user

# Actualizar
# ----------
@router.put("/edit")
async def user(user: User):
    for index, user_item in enumerate(users_list):
        if user_item.id == user.id:
            users_list[index] = user
            return user
    return {"error": "Usuario no encontrado, no se ha podido actualizar el usuario"}

@router.delete("/delete/{id}")
async def user(id: int):
    for index, user_item in enumerate(users_list):
        if user_item.id == id:
            user_temp = user_item
            del users_list[index]
            return user_temp
    return {"error" : "Usuario no encontrado"}

# Funcion para buscar y retornar un usuario
# -----------------------------------------
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se han econtrado el usuario especificado"}