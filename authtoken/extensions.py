from django.utils.crypto import get_random_string
import hashlib


def generate_token():
    prefix = get_random_string(12)
    hash_object = hashlib.sha224(prefix.encode())
    token =  hash_object.hexdigest()
    return token