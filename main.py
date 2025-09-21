import os
import httpx
from fastapi import FastAPI

app = FastAPI()

LTA_API_KEY = os.getenv("LTA_API_KEY")

@app.get("/")
async def root():
    return {"message": "Didi took an L"}

@app.get("/carparks")
def get_carparks():
    url = "https://datamall2.mytransport.sg/ltaodataservice/CarParkAvailabilityv2"
    headers = {"AccountKey": LTA_API_KEY}
    response = httpx.get(url, headers=headers)

    if response.status_code != 200:
        return {"error": "Failed to fetch data"}
    
    data = response.json()
    return data