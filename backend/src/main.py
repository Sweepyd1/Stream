from fastapi import FastAPI
import uvloop
import asyncio 
import uvicorn
import os
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Stream backend app")


origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

# storage_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'storage_files'))

# app.mount("/assets", StaticFiles(directory=storage_directory), name="storage_files")


if __name__ == "__main__":
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    uvicorn.run(app)

