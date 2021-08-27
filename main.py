from fastapi import FastAPI
from database.database import Database
import os


app = FastAPI()
test = Database(os.env["DB_KEY"], "dev_db")

@app.get("/db_add/{title}/{content}")
async def add(title, content):
    test.add(title,content)
    return "added"

@app.get("/db_fetch/{title}/")
async def fetch(title, ):
    data = test.fetch(title)
    return data

@app.get("/db_remove/{title}/")
async def remove(title ):
    data = test.remove(title)
    return "data removed"