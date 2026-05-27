from pydantic import BaseModel, Field, ConfigDict

class Aeroporto(BaseModel):
    id: int
    codice: int
    citta: int

class AeroportoCreate(BaseModel):
    codice: str = Field(min_length=3)
    citta: str
