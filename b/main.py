from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/download/{file_path}")
async def download_file(file_path:str):
  return FileResponse(path=file_path)

@app.get("/get_files/")
async def getfiles():
   res = []
   for filename in os.listdir("assets"):
      res.append(filename)
   return res
