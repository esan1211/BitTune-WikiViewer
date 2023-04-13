# TODO(Project 1): Implement Backend according to the requirements.
"""Creates the backend system for the wiki's specific functions

Adds text files to bucket, handles user login and sign up, returns images, and
sets up the route of the different wiki pages.

Typical usage example:

  backend = Backend()
  user = User()
"""
import os
import pathlib
import io
import base64
from pathlib import Path
from google.cloud import storage
import hashlib


class User:
    """Creates a Class that describes a user interacts with the login an sign-up functionality.

    Attributes:
        username: A string with the username of the user
        password: A string with the password of the user
    """

    def __init__(self, username, password):
        """Inits User instance with username and password."""
        self.username = username
        self.password = password


class Backend:
    """Creates a Class that describes the functionality of the wikiviewer

    Attributes:
        
    """

    def __init__(self):
        """Inits Backend instance """
        pass

    def get_wiki_page(self, name):  #Danny
        """Gets specific text file chosen from GCS Bucket to dispaly as pages"""
        storage_client = storage.Client()
        bucket = storage_client.bucket("bt-wikiviewer-content")
        blob = bucket.get_blob(name)
        #print("hello", blob)
        with blob.open() as f:
            return f.read()

    def get_all_page_names(self):  #Danny
        """Shows user all available pages that are viewable"""
        storage_client = storage.Client()
        blobs = storage_client.list_blobs("bt-wikiviewer-content")

        blob_name_lst = []

        for blob in blobs:
            if (blob.name.endswith(".txt")):
                blob_name_lst.append(blob.name)

        #print(blob_name_lst)

        return blob_name_lst

    def upload(self, file_uploaded):  #Enrique
        """Allows user to upload a text file into the GCS Bucket"""
        storage_client = storage.Client()
        bucket = storage_client.bucket("bt-wikiviewer-content")
        if (file_uploaded.endswith(".txt")):
            filename = "%s%s" % ('', file_uploaded)
            blob = bucket.blob(filename)
            basedir = os.path.abspath(os.path.dirname(file_uploaded))
            with open(file_uploaded, 'rb') as f:
                blob.upload_from_file(f)
        pass

    def sign_up(self, username, password):  #Asis
        """Allows user to sign up"""
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
        return True

    def sign_in(self, username, password):  #Asis
        """Once the user has an account, they can login using their credentials"""
        hashed = hashlib.sha256(password.encode()).hexdigest()
        bucket_name = "bt-wikiviewer-users_passwords"

        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)

        blobs = storage_client.list_blobs(bucket_name)
        for blob in blobs:
            if username == blob.name:
                blob = bucket.get_blob(username)
                with blob.open("r") as f:
                    stored = f.read()
                if stored == hashed:
                    return True

    def get_image(self, image):  #Enrique
        """Encodes image from GCS Bucket in order to view in pages"""
        storage_client = storage.Client()
        bucket = storage_client.bucket("bt-wikiviewer-content")
        blobs = storage_client.list_blobs("bt-wikiviewer-content")
        for blob in blobs:
            if blob.name == image:
                blob = bucket.get_blob(image)
                with blob.open("rb") as f:
                    encoded_string = base64.b64encode(f.read())
                    return encoded_string
        print("Does not exist")
        pass

    def get_discussion_post(self,post): #Enrique
        """Gets a specific discussion posts page"""
        storage_client = storage.Client()
        bucket = storage_client.bucket("bt-wikiviewer-discussions")
        blob = bucket.get_blob(post)
        with blob.open() as f:
            return f.read()

    def get_all_discussion_posts(self): #Enrique
        """Shows user all available discussion posts"""
        storage_client = storage.Client()
        blobs = storage_client.list_blobs("bt-wikiviewer-discussions")
        discussion_list = []
        for blob in blobs:
            if (blob.name.endswith(".txt")):
                discussion_list.append(blob.name)
        print(discussion_list)
        return discussion_list

    def upload_discussion_post(self, file_uploaded): #Enrique
        """Allows user to upload a text file discussion into the GCS Discussions Bucket"""
        storage_client = storage.Client()
        bucket = storage_client.bucket("bt-wikiviewer-discussions")
        if (file_uploaded.endswith(".txt")):
            filename = "%s%s" % ('', file_uploaded)
            blob = bucket.blob(filename)
            with open(file_uploaded, 'rb') as f:
                blob.upload_from_file(f)
        pass
