# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import create_tables, delete_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Tables deleted")
    await create_tables()
    print("Tables created")
    yield
    print("Shutting down")

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
