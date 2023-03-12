# TODO(Project 1): Implement Backend according to the requirements.
import os
import pathlib
from pathlib import Path
from google.cloud import storage

class Backend:

    def __init__(self):
        pass
        
    def get_wiki_page(self, name):
        pass

    def get_all_page_names(self):
        pass

    def upload(self, file_uploaded): #Enrique
        storage_client = storage.Client()
        bucket = storage_client.bucket("bt-wikiviewer-content")
        if(file_uploaded.endswith(".txt")):
            filename = "%s%s" % ('',file_uploaded)
            blob = bucket.blob(filename)
            with open(file_uploaded,'rb') as f:
                blob.upload_from_file(f)
                print("Uploaded")

        

        pass

    def sign_up(self):
        pass

    def sign_in(self):
        pass

    def get_image(self):
        pass

