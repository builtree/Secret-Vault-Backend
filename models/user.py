import os
import datetime
from typing import List
from pydantic import BaseModel
from database.database import Database
from helper.auth import AuthHandler

class UserData(BaseModel):
    name : str
    password : str
    last_updated : datetime.datetime


class User(BaseModel):
    
    id : str
    username : str
    password_hash : str
    vault_data : List[UserData]
    
    
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
    
