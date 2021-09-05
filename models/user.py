import os
import datetime
from typing import List, Optional
from pydantic import BaseModel
from database.database import Database
from helper.auth import AuthHandler

class UserData(BaseModel):
    name : str
    password : str
    last_updated : datetime.datetime


class User(BaseModel):
    
    id : Optional[str]
    username : str
    password : str
    password_hash : Optional[str]
    vault_data : Optional[List[UserData]]
    
    
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
    
