import os
from fastapi import FastAPI
from database.database import Database
from helper.hashing import hash
from helper.auth import AuthHandler
from models.user import User 

app = FastAPI()
user_db = Database(os.environ.get('DETA'), 'users')
auth_handler = AuthHandler() 



@app.post("/signup")
async def signup(user : User):
    user_id = hash(user.username, os.environ.get('USER_ID_HASH_SECRET'))
    
    if not user_db.fetch(user_id):
        user.password_hash = auth_handler.get_password_hash(user.password)
        user_db.add(
            user_id,
            user.dict(exclude = {'password'})
        )
        
        return {'status': 'success'}
        
    else :
        return {'status': 'already exists'}
    
    
@app.post("/login")
async def login(user : User):
    user_id = hash(user.username, os.environ.get('USER_ID_HASH_SECRET'))
    
    
    try:
        user_from_db = user_db.fetch(user_id)
        user_from_db['value']['id'] = user_id
        print(user_from_db)

        
        if auth_handler.verify_password(user.password, user_from_db['value']['password_hash']):
            return {'status': 'success'}
        return {'status': 'wrong password'}
    
    except :
        return {'status': 'user not found'}