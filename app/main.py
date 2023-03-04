# app/main.py
from fastapi import FastAPI

from app.database import connect_to_mongo, close_mongo_connection
from app.routes import items, users


app = FastAPI()

app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(users.router, prefix="/users", tags=["users"])


@app.on_event("startup")
async def startup_event():
    await connect_to_mongo(app)


@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection(app)

