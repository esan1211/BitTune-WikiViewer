# TODO(Project 1): Implement Backend according to the requirements.
import os
import pathlib
from pathlib import Path
from google.cloud import storage
import hashlib

class Backend:

    def __init__(self):
        pass
        
    def get_wiki_page(self, name): #Danny
        storage_client = storage.Client()
        bucket = storage_client.bucket("bt-wikiiewer-content")
        blob = bucket.get_blob(name + ".txt")
        with blob.open() as f:
            return f

    def get_all_page_names(self):#Danny
        storage_client = storage.Client()
        bucket = storage_client.bucket("bt-wikiiewer-content")
        blobs = bucket.list_blobs("bt-wikiiewer-content")

        blob_name_lst = []

        for blob in blobs:
            blob_name_lst.append(blob.name)
            
        return blob_name_lst
        

    def upload(self, file_uploaded): #Enrique
        storage_client = storage.Client()
        bucket = storage_client.bucket("bt-wikiviewer-content")
        if(file_uploaded.endswith(".txt")):
            filename = "%s%s" % ('',file_uploaded)
            blob = bucket.blob(filename)
            with open(file_uploaded,'rb') as f:
                blob.upload_from_file(f)
        pass

    def sign_up(self, user, password): #Asis
        bucket_name = "bt-wikiviewer-users_passwords"
        
        storage_client = storage.Client()

        blobs = storage_client.list_blobs(bucket_name)
        if user not in blobs: 
            bucket = storage_client.bucket(bucket_name)
            blob = bucket.blob(user)

            hashed = hashlib.sha256(password.encode()).hexdigest()

            with blob.open("w") as f:
                f.write(hashed)
        else:
            return False

    def sign_in(self, user, password): #Asis
        bucket_name = "bt-wikiviewer-users_passwords"

        storage_client = storage.Client()

        bucket = storage_client.bucket(bucket_name)

        blobs = storage_client.list_blobs(bucket_name)
        for b in blobs:
            if b == user:
                blob = bucket.blob(user)
                with blob.open("r") as f:
                    hashed = f.read()
                if hashed == hashlib.sha256(password.encode()).hexdigest():
                    return True
                else:
                    return False

    def get_image(self, image): #Enrique
        storage_client = storage.Client()
        blobs = storage_client.list_blobs("bt-wikiviewer-content")
        for blob in blobs:
            if blob.name:
                print("Success")
                return image
            else:
                print("Image does not exist")
                return
        pass

    

