from google.cloud import storage
import hashlib

class Backend:

    def __init__(self):
        pass
        
    def get_wiki_page(self, name): #Danny
        bucket = storage.bucket("bt-wikiiewer-content")
        blob = bucket.get_blob(name + ".txt")
        with blob.open() as f:
            return f

    def get_all_page_names(self):#Danny
        pass

    def upload(self):
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

    def sign_in(self): #Asis
        pass

    def get_image(self):
        pass

