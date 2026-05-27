from pydantic import BaseModel, Field, ConfigDict

class Aeroporto(BaseModel):
    id: int
    codice: int
    citta: int

class AirportCreate(BaseModel):
    codice: str = Field(min_length=3)
    citta: str

class PaginatedAirports(BaseModel):
    page: int
    size: int
    total: int
    data: str
    