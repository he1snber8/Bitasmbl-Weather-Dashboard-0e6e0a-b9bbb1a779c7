from pydantic import BaseModel
from datetime import datetime

class WeatherData(BaseModel):
    city: str
    timestamp: datetime
    temperature: float
