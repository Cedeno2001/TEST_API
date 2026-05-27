from fastapi import APIRouter, HTTPException
from typing import List
from ..models import Airport, AirportCreate
from ..Aeroporti_api import crud

router = APIRouter(prefix="/airports", tags=["Airports"])


@router.get("", response_model=List[Airport])
def list_airports(page: int = 1, size: int = 10):
    return crud.get_airports(page, size)


@router.get("/{airport_id}", response_model=Airport)
def get_airport(airport_id: int):
    airport = crud.get_airport(airport_id)
    if not airport:
        raise HTTPException(status_code=404, detail="Airport not found")
    return airport


@router.post("", response_model=Airport, status_code=201)
def create_airport(airport: AirportCreate):
    return crud.create_airport(airport.dict())