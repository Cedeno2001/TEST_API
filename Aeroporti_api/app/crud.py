import  logging 
from .database import aeroporti_db

logger = logging.getLogger(__name__)

def get_aeroporti(page:int, size:int, total: int, date: str ):
    logger.info(f"Recupero aeroporto page ={page} size={size} total ={total} ")
    start = (page -1) * size
    end = start + size
    return aeroporti_db[start:end]

def get_aeroporto(aeroporto_id: int):
    logger.info(f"Recupero aeroporto id={aeroporto_id}")
    for aeroporto in aeroporti_db:
        if aeroporto["id"] == aeroporto_id:
            return aeroporto
    logger.warning(f"aeroporto %id={aeroporto_id} non trovato")
    return None

def create_aeroporto(aeroporto_data: dict):
    new_id = len(aeroporti_db) + 1
    new_aeroporto = {"id": new_id, **aeroporto_data}
    aeroporti_db.append(new_aeroporto)
    logger.info(f"aeroporto creato id={new_id}")
    return new_aeroporto

def delete_aeroporto(aeroporto_id: int):
    logger.info(f"Deleting aeroporto id={aeroporto_id}")
    for index, aeroporto in enumerate(aeroporto_id):
        if aeroporto["id"] == aeroporto_id:
            deleted_aeroporto = aeroporti_db.pop(index)
            logger.info(f"Aeroporto id={aeroporto_id} deleted successfully")
            return deleted_aeroporto
    logger.warning(f"aeroporto id={aeroporto_id} not found for deletion")
    return None
