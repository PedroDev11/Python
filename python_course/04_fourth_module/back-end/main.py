# .\env\Scripts\activate.bat
# py -m uvicorn main:app --reload

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return "Hola"

productos = [
    {"id": 1, "name": "Leche", "precio": 20, "cantidad": 50},
    {"id": 2, "name": "Cheetos", "precio": 12, "cantidad": 20},
    {"id": 3, "name": "Huevo", "precio": 39, "cantidad": 80},
    {"id": 4, "name": "Aceite", "precio": 40, "cantidad": 40},
]

@app.get("/productos")
async def products():
    return productos

@app.get("/productos/{id}")
async def productId(id: int):
    for product in productos:
        if product["id"] == id:
            return product
    return {"message": f"No se encontró el prodcuto con el id: {id}"}

@app.post("/productos")
async def createProdcut(product: dict):
    productos.append(product)
    return {"message": f"se agregó correctamente el prodcuto: {product}"}

@app.put("/productos/{id}")
async def updateProdcut(id: int, productBody: dict):
    for product in productos:
        if product["id"] == id:
            product = productBody
            return productBody
    return {"message": f"no actualizó correctamente el prodcuto: {product}"}

@app.delete("/productos/{id}")
async def deleteProdcut(id: int):
    for product in productos:
        if product["id"] == id:
            productos.remove(product)
            return productos
    return {"message": f"no se eliminó correctamente el prodcuto: {product}"}