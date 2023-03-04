from fastapi import APIRouter, Depends
from ..dependencies import get_db
from ..database import NewTableDB
from ..models import NewTable

router = APIRouter()

@router.get("/new_table/{id}")
async def read_new_table(id: str, db: NewTableDB = Depends(get_db)):
    new_table = db.get_by_id(id)
    return new_table
