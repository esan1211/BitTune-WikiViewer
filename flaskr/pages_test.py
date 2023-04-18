from flaskr import create_app
from unittest.mock import MagicMock, patch
from pathlib import Path
import pytest


# See https://flask.palletsprojects.com/en/2.2.x/testing/
# for more info on testing
@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
    })
    return app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def bucket():
    return MagicMock()


# TODO(Checkpoint (groups of 4 only) Requirement 4): Change test to
# match the changes made in the other Checkpoint Requirements.


# TODO(Project 1): Write tests for other routes.
def test_home_page(client):  #Enrique
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"<title>Wiki Music Museum</title>" in resp.data


def test_upload_page(client, app):  #Enrique
    resp = client.post("/upload", data={"myfile": "test.txt"})
    assert b"<h2>Upload</h2>" in resp.data
    assert resp.status_code == 200

def test_search_bar_page(client): #Asis
    resp = client.get('/search')
    assert resp.status_code == 200
    assert b'<h1 style="font-size: 40px;"> Search</h1>' in resp.data

