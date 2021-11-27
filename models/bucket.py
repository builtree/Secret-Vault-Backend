import os
from pydantic import BaseModel
from typing import Optional
from database.database import Database
from helper.hashing import hash

user_db = Database(os.environ.get('DETA'), 'users')
bucket_db = Database(os.environ.get('DETA'), 'bucket')


class Bucket(BaseModel):
    id: Optional[str]
    bucket_name: str
    username: str


def new_bucket(username, bucket_name):
    user_id = hash(username, os.environ.get('USER_ID_HASH_SECRET'))
    bucket_id = hash(username + '_' + bucket_name,
                     os.environ.get('BUCKET_ID_HASH_SECRET'))

    buckets = user_db.fetch(user_id)['bucket_list']
    buckets.append(bucket_name)

    user_data = {
        'bucket_list': buckets
    }

    bucket_data = {
        'bucket_name': bucket_name,
        'bucket_list': []
    }

    user_db.add(user_id, user_data)
    bucket_db.add(bucket_id, bucket_data)


