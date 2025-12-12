from fastapi import FastAPI
from .models import WeatherData

app = FastAPI()

@app.get("/weather/current", response_model=WeatherData)
async def get_current(city: str):
    return WeatherData(city=city, timestamp=0, temperature=0)
