import os
from fastapi import FastAPI
from starlette.responses import Response
from database.database import Database
from helper.hashing import hash
from helper.auth import AuthHandler
from models.user import User 
from helper.token_handler import generate_token, verify_token 

app = FastAPI()
user_db = Database(os.environ.get('DETA'), 'users')
auth_handler = AuthHandler() 



@app.post("/signup")
async def signup(user : User):
    user_id = hash(user.username, os.environ.get('USER_ID_HASH_SECRET'))
    
    try : 
        if not user_db.fetch(user_id):
            user.id = user_id
            user.password_hash = auth_handler.get_password_hash(user.password)
            user_db.add(
                user_id,
                user.dict(exclude = {'password'})
            )
            token = generate_token(user.username)
            return {
                'status': 'success',
                'token' : token
                }
            
        else :
            return {'status': 'already exists'}
    except :
        return Response("Internal server error", status_code=500)
        
        
    
@app.post("/login")
async def login(user : User):
    user_id = hash(user.username, os.environ.get('USER_ID_HASH_SECRET'))
    
    
    try:
        user_from_db = user_db.fetch(user_id)
        user_from_db['value']['id'] = user_id
        print(user_from_db)

        
        if auth_handler.verify_password(user.password, user_from_db['value']['password_hash']):
            token = generate_token(user.username)
            return {
                'status': 'success',
                'token' : token
                }
        return {'status': 'wrong password'}
    
    except :
        return {'status': 'user not found'}