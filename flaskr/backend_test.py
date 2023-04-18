from flaskr.backend import Backend
from unittest.mock import MagicMock, patch, mock_open
from google.cloud import storage
import pytest


# TODO(Project 1): Write tests for Backend methods.
@patch('google.cloud.storage.Client')
def test_upload(mock_client): #Enrique
    backend = Backend()
    mock_data = b"Test"
    mock_file = MagicMock()
    mock_file.endswith.return_value = "txt"
    with patch("builtins.open", mock_open(read_data=mock_data)) as mock_open_func:
        backend.upload(mock_file)
    mock_open_func.assert_called_once_with(mock_file, "rb")


@patch('google.cloud.storage.Client')
def test_get_image_success(mock_client): #Enrique
    backend = Backend()
    mock_bucket_name = "test"
    mock_blob = MagicMock()
    mock_blob.name = "image.jpg"
    mock_bucket = MagicMock()
    mock_client.return_value.get_bucket.return_value = mock_bucket
    mock_bucket.name = mock_bucket_name
    mock_bucket.list_blobs.return_value = [mock_blob]
    mock_client.return_value = mock_bucket
    with patch("base64.b64encode") as encode:
        result = backend.get_image("image.jpg")
        mock_encoding = backend.get_image("image.jpg")
        assert result == mock_encoding


@patch('google.cloud.storage.Client')
def test_get_image_fail(mock_client): #Enrique
    backend = Backend()
    mock_bucket_name = "test"
    mock_blob = MagicMock()
    mock_blob.name = "image.jpg"
    mock_bucket = MagicMock()
    mock_client.return_value.get_bucket.return_value = mock_bucket
    mock_bucket.name = mock_bucket_name
    mock_bucket.list_blobs.return_value = [mock_blob]
    mock_client.return_value = mock_bucket
    with patch("base64.b64encode") as encode:
        mock_encoding = None
        result = backend.get_image(" ")
        assert result == mock_encoding

@patch('google.cloud.storage.Client') #Enrique
def test_upload_discussion_post(mock_client):
    backend = Backend()
    mock_data = b"Test"
    mock_file = MagicMock()
    mock_file.endswith.return_value = "txt"
    with patch("builtins.open", mock_open(read_data=mock_data)) as mock_open_func:
        backend.upload_discussion_post(mock_file)
    mock_open_func.assert_called_once_with(mock_file, "rb")

@patch('google.cloud.storage.Client') #Enrique
def test_get_all_discussion_posts(mock_client):
    backend = Backend()
    mock_data = b"Test"
    mock_bucket_name = "test"
    mock_blob = MagicMock()
    mock_blob.name = "discussion.txt"
    mock_bucket = MagicMock()
    mock_client.return_value.get_bucket.return_value = mock_bucket
    mock_bucket.name = mock_bucket_name
    mock_bucket.list_blobs.return_value = [mock_blob]
    mock_client.return_value = mock_bucket
    with patch("builtins.open", mock_open(read_data=mock_data)) as mock_open_func:
        result = backend.get_all_discussion_posts()
    assert result == [mock_blob.name]

"""
@patch('google.cloud.storage.Client') #Enrique
def test_get_discussion_posts(mock_client):
    backend = Backend()
    mock_data = b"Test"
    mock_bucket_name = "test"
    mock_blob = MagicMock()
    mock_blob.name = "discussion.txt"
    mock_bucket = MagicMock()
    mock_client.return_value.get_bucket.return_value = mock_bucket
    mock_bucket.name = mock_bucket_name
    mock_bucket.list_blobs.return_value = [mock_blob]
    mock_client.return_value = mock_bucket
    with patch("builtins.open",mock_open(read_data=mock_data)) as mock_open_func:
        print(mock_blob.name)
        result = backend.get_discussion_post(mock_blob)
        print(result.name)
    assert result == mock_blob.name
    """
