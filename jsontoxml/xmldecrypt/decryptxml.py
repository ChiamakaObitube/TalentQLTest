from cryptography.fernet import Fernet
import base64
import os

def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("encryptjson/secret/key.key", "rb").read()

def decrypt(filename, key):

    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    
    decrypted_data = f.decrypt(encrypted_data)

    with open(filename, "wb") as file:
        file.write(decrypted_data)

    #write_key()
load_key()
key = load_key()
file = "encryptjson/data_object"
decrypt(file, key)
    