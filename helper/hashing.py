import hmac
import hashlib


def hash(string, secret):
    hash = hmac.new(
        bytes(secret, 'utf-8'),
        bytes(string, 'utf-8'),
        hashlib.sha256)
    return hash.hexdigest()