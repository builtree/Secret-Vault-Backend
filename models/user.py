import os
import datetime
from typing import List, Optional
from pydantic import BaseModel, validator
from database.database import Database
from helper.auth import AuthHandler
from helper.hashing import hash

auth_handler = AuthHandler()

class UserData(BaseModel):
    name : str
    password : str
    last_updated : datetime.datetime


class User(BaseModel):
    
    id : Optional[str]
    username : str
    password : Optional[str]
    password_hash : Optional[str]
    bucket_list : Optional[List]
    
    @validator('password_hash', pre=True, always=True)
    @classmethod
    def generate_password_hash(cls, value, values):
        value = auth_handler.get_password_hash(values['password'])
        return value
    
    @validator('bucket_list', pre=True, always=True)
    @classmethod
    def init_bucket(cls, value):
        return []


class UserAuth():
    def __init__(self, user, entered_password):
        self.user = user
        auth_handler = AuthHandler()

        print(f'entered password : {entered_password}')
        
        if auth_handler.verify_password(entered_password, self.user.password_hash):
            print('login OK')
        else :
            print('login failed')
            
        pass
    
