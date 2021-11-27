from deta import Deta
import os
# from cryptography.fernet import Fernet


# we'll input this from user later
# passphrase = Fernet.generate_key()

class Database:
    def __init__(self, key, db_name):
        deta = Deta(key)
        self.db = deta.Base(db_name)
        # self.fernet = Fernet(passphrase)
    
        self.key = key
        self.name = db_name
        # self.db = db
    
    def add(self,key, data):
        data.update({
            "key" : key
        })
        # enc = self.fernet.encrypt(content.encode())
        self.db.put(data)
    
    def fetch(self, item):
        
        item = self.db.get(item)
        # pwd = self.fernet.decrypt(item["value"]).decode()
        return item

    def remove(self,item):
        self.db.delete(item)

# test = Database(os.environ["DB_KEY"])
# print(os.environ["DB_KEY"])

