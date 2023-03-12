# TODO(Project 1): Implement Backend according to the requirements.
import os
import pathlib
from pathlib import Path
from google.cloud import storage
import hashlib

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Backend:
    def __init__(self):
        pass
        
    def get_wiki_page(self, name): #Danny
        storage_client = storage.Client()
        bucket = storage_client.bucket("bt-wikiviewer-content")
        blob = bucket.get_blob(name)
        #print("hello", blob)
        with blob.open() as f:
            return f.read()

    def get_all_page_names(self): #Danny
        storage_client = storage.Client()
        blobs = storage_client.list_blobs("bt-wikiviewer-content")

        blob_name_lst = []

        for blob in blobs:
            if(blob.name.endswith(".txt")):
                blob_name_lst.append(blob.name)

        #print(blob_name_lst)
            
        return blob_name_lst
        

    def upload(self, file_uploaded): #Enrique
        storage_client = storage.Client()
        bucket = storage_client.bucket("bt-wikiviewer-content")
        if(file_uploaded.endswith(".txt")):
            filename = "%s%s" % ('',file_uploaded)
            blob = bucket.blob(filename)
            basedir = os.path.abspath(os.path.dirname(file_uploaded))
            print(file_uploaded)
            with open(file_uploaded,'rb') as f:
                blob.upload_from_file(f)
        pass

    def sign_up(self, username, password): #Asis
        hashed = hashlib.sha256(password.encode()).hexdigest()

        bucket_name = "bt-wikiviewer-users_passwords"
        
        storage_client = storage.Client()

        blobs = storage_client.list_blobs(bucket_name)

        for blob in blobs:
            if username == blob.name: 
                return None
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(username)
        with blob.open('w') as f:
            f.write(hashed)

    def sign_in(self, username, password): #Asis
        hashed = hashlib.sha256(password.encode()).hexdigest()
        bucket_name = "bt-wikiviewer-users_passwords"

        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)

        blobs = storage_client.list_blobs(bucket_name)
        for blob in blobs:
            if username == blob.name:
                #print('HELLO')
                blob = bucket.get_blob(username)
                with blob.open("r") as f:
                    stored = f.read()
                    #print('HELLO' + stored)
                if stored == hashed:
                    return True
            
    def get_image(self, image): #Enrique
        storage_client = storage.Client()
        blobs = storage_client.list_blobs("bt-wikiviewer-content")
        for blob in blobs:
            print(blob.name)
            if blob.name == image:
                print("Success")
                print(blob)
                return blob
        print("Does not exist")
        pass
    

