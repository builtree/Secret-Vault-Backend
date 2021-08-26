pip install deta
from deta import Deta


class Database:
    def __init__(self, key, db_name):
        self.key = key
        self.name = name

        deta = Deta(key)
        db = deta.Base(name)    
    def add(title, content):
        db.put({title:content})
    
    def fetch(item):
        item = db.get(item) 
        return item

    def remove(item):
        db.delete(item)
