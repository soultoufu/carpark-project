from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Didi took an L"}

@app.get("/carparks")
async def get_carparks():
    return [
        {"id": 1, "name": "HDB Lot A", "price": 1.20, "availability": 35},
        {"id": 2, "name": "HDB Lot B", "price": 2.00, "availability": 32}
    ]