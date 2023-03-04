from fastapi import APIRouter, HTTPException, Depends, status
from bson.objectid import ObjectId
from datetime import datetime

from database import db, users_collection
from auth import get_password_hash, verify_password, create_access_token, get_current_user


router = APIRouter()

@router.post("/users")
async def create_user(username: str, password: str):
    hashed_password = get_password_hash(password)
    user = {
        "username": username,
        "password": hashed_password,
        "created_at": datetime.utcnow(),
    }
    result = users_collection.insert_one(user)
    user["_id"] = str(result.inserted_id)
    return user


@router.post("/login")
async def login(username: str, password: str):
    user = users_collection.find_one({"username": username})
    if user is None or not verify_password(password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(user["_id"])
    return {"access_token": access_token}
