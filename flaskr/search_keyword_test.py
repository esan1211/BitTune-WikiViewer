from flaskr.backend import Backend
from unittest.mock import MagicMock, patch, mock_open
from google.cloud import storage
import pytest

'''I was tasked to create a search bar for Daniel's User Pages, so this test doubles for me fulfilling the User Pages R1
    requirement that I was assigned, as well as Requirement 1 in the Merge Requests checkpoint"
'''
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
