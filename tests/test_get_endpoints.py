
import json
import pytest
from flask_tweet_api.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_data(as_text=True) == 'Hello World'

def test_get_all_tweets(client):
    response = client.get('/tweets')
    assert response.status_code == 200
    assert len(json.loads(response.get_data(as_text=True))) == len(client.application.tweets_data)

def test_get_filtered_tweets(client):
    response = client.get('/tweets_filtered?filter=some_keyword')
    assert response.status_code == 200

def test_get_tweet_by_id_successful(client):
    response = client.get('/tweet/1')
    assert response.status_code == 200

def test_get_tweet_by_id_unsuccessful(client):
    response = client.get('/tweet/999')
    assert response.status_code == 404
