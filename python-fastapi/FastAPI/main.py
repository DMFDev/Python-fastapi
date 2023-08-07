from fastapi import FastAPI
from routers import products
from routers import users

app = FastAPI()


# Routers
# -------
app.include_router(products.router)
app.include_router(users.router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}


# documentacion con Swagger
# http://127.0.0.1:8000/docs#/