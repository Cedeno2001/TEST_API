from fastapi import APIRouter, HTTPException
from typing import List
from models import aeroporto, aeroportoCreate
from ...Aeroporti_api.tests import crud

router = APIRouter(prefix="/airports", tags=["Airports"])


@router.get("", response_model=List[aeroporto])
def list_aeroporto(page: int = 1, size: int = 10):
    return crud.get_airports(page, size)


@router.get("/{airport_id}", response_model=aeroporto)
def get_aeroporto(airport_id: int):
    airport = crud.get_airport(airport_id)
    if not airport:
        raise HTTPException(status_code=404, detail="Airport not found")
    return airport


@router.post("", response_model=aeroporto, status_code=201)
def create_aeroporto(airport: aeroportoCreate):
    return crud.create_airport(airport.dict())