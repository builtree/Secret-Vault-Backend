import os
import jwt 
from datetime import datetime, timedelta

def genrate_token(username, time_delta = timedelta(days=1)):
    start_time = datetime.utcnow()
    end_time = start_time + time_delta
    token = {
        "username" : username,
        "start_time" : start_time.timestamp(),
        "end_time" : end_time.timestamp(),
    }
    
    return jwt.encode(token, os.environ.get("TOKEN_SECRET"),algorithm="HS256")


def verify_token(username,encoded_token):
    try :
        decoded_token = jwt.decode(encoded_token, os.environ.get("TOKEN_SECRET"), ["HS256"])
        if decoded_token['username'] == username and datetime.now().timestamp() < decoded_token['end_time']:
            return True
        return False
        
    except :
        return False