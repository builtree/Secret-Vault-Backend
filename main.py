import os
from fastapi import FastAPI, Request
from starlette.responses import Response
from database.database import Database
from helper.hashing import hash
from helper.auth import AuthHandler
from models.user import User
from models.bucket import Bucket
from models.item import Item
from helper.token_handler import generate_token, verify_token

app = FastAPI()
user_db = Database(os.environ.get('DETA'), 'users')
bucket_db = Database(os.environ.get('DETA'), 'bucket')
auth_handler = AuthHandler()


@app.post("/signup")
async def signup(user: User):
    user_id = hash(user.username, os.environ.get('USER_ID_HASH_SECRET'))

    try:
        if not user_db.fetch(user_id):
            user.id = user_id
            # user.password_hash = auth_handler.get_password_hash(user.password)
            user_db.add(
                user_id,
                user.dict(exclude={'password'})
            )
            token = generate_token(user.username)
            return {
                'status': 'success',
                'token': token
            }

        else:
            return Response("User already exists", status_code=401)
    except:
        return Response("Internal server error", status_code=500)


@app.post("/login")
async def login(user: User):
    user_id = hash(user.username,
                   os.environ.get('USER_ID_HASH_SECRET'))

    try:
        user_from_db = user_db.fetch(user_id)

        if auth_handler.verify_password(user.password, user_from_db['password_hash']):
            token = generate_token(user.username)
            return {
                'status': 'success',
                'token': token
            }

        return Response("Failed login", status_code=401)

    except:
        return Response("User not found", status_code=404)


@app.get("/get_buckets/{username}")
async def get_buckets(username: str, request: Request):
    token = request.headers.get('token')

    if verify_token(username, token):
        user_id = hash(username,
                       os.environ.get('USER_ID_HASH_SECRET'))
        try:
            user_from_db = user_db.fetch(user_id)
            bucket_list = user_from_db['bucket_list']
            return {'buckets': bucket_list}

        except:
            return Response("Something went wrong", status_code=401)
    else:
        return Response("Failed login", status_code=401)


@app.post("/add_bucket")
async def add_bucket(bucket: Bucket, request: Request):

    token = request.headers.get('token')

    if verify_token(bucket.username, token):
        user_id = hash(bucket.username, os.environ.get('USER_ID_HASH_SECRET'))
        bucket_id = hash(bucket.username + '_' + bucket.bucket_name,
                         os.environ.get('BUCKET_ID_HASH_SECRET'))

        bucket_data = {
            'bucket_name': bucket.bucket_name,
            'user': bucket.username,
            'bucket_list': {}
        }

        user_from_db = user_db.fetch(user_id)
        if bucket.bucket_name not in user_from_db['bucket_list']:
            user_from_db['bucket_list'].append(bucket.bucket_name)
        user_db.add(user_id, user_from_db)
        bucket_db.add(bucket_id, bucket_data)

        return {"message": "success"}

    else:
        return {"message": "not verified",
                "username": bucket.username,
                "token": token}


@app.post("/add_item")
async def add_item(item: Item, request: Request):
    token = request.headers.get('token')

    if verify_token(item.username, token):
        bucket_id = hash(item.username + '_' + item.bucket_name,
                         os.environ.get('BUCKET_ID_HASH_SECRET'))

        bucket_from_db = bucket_db.fetch(bucket_id)
        data = {item.name: {
            'item_name': item.name,
            'value': item.value
        }}

        bucket_from_db['bucket_list'].update(data)

        bucket_db.add(bucket_id, bucket_from_db)


@app.get("/get_items/{username}/{bucket_name}")
async def get_items(username: str, bucket_name: str, request: Request):
    token = request.headers.get('token')

    if verify_token(username, token):
        bucket_id = hash(username + '_' + bucket_name,
                         os.environ.get('BUCKET_ID_HASH_SECRET'))

        bucket_from_db = bucket_db.fetch(bucket_id)

        if bucket_from_db is None:
            return Response("Bucket not found")

        res = bucket_from_db['bucket_list']

        return res
