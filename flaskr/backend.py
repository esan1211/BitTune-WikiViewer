from google.cloud import storage

class Backend:

    def __init__(self):
        pass
        
    def get_wiki_page(self, name): #Danny
        bucket = storage.bucket("bt-wikiiewer-content")
        blob = bucket.get_blob(name + ".txt")
        with blob.open() as f:
            return f

    def get_all_page_names(self):#Danny
        bucket = storage.bucket("bt-wikiiewer-content")
        storage_client = storage.Client()
        blobs = storage_client.list_blobs("bt-wikiiewer-content")

        blob_name_lst = []

        for blob in blobs:
            blob_name_lst.append(blob.name)
            
        return blob_name_lst
        

        pass

    def upload(self):
        pass

    def sign_up(self):
        pass

    def sign_in(self):
        pass

    def get_image(self):
        pass

