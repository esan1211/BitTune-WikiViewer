from flaskr.backend import Backend
from unittest.mock import MagicMock, patch, mock_open
from google.cloud import storage
import pytest

@patch('google.cloud.storage.Client')
def test_search_keyword(mock_client): 
    backend = Backend()
    mock_data = b"My name is Asis"
    with patch("builtins.open", mock_open(read_data=mock_data)) as mock_open_func:
        assert backend.search_keyword('name') == [mock_open_func]
     

def test_search_result(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"<h2>Museum Walls</h2>" in resp.data
