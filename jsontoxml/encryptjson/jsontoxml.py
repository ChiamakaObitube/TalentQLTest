import json
import os
from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson
from cryptography.fernet import Fernet


 # create a directory for encryptedxml
path = "jsontoxml/encryptedxml"
try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)

data = readfromjson("jsontoxml/encryptjson/sample.json")
data_object = str((json2xml.Json2xml(data).to_xml()))
# print(data_object)

with open("jsontoxml/encryptedxml/data_object", "w") as file:
    file.write(data_object)

def write_key():
    # create a directory for secrets
    path = "jsontoxml/secret"
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)
    # generate key
    key = Fernet.generate_key()
    with open("jsontoxml/secret/key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("jsontoxml/secret/key.key", "rb").read()

def encrypt(filename, key):

    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    with open(filename, "wb") as file:
        file.write(encrypted_data)
    
write_key()
key = load_key()
file = "jsontoxml/encryptedxml/data_object"

encrypt(file, key)
