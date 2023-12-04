

import json
import pytest
from flask_tweet_api.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_tweet_successful(client):
    new_tweet = {'id': 101, 'text': 'This is a new tweet.'}
    response = client.post('/tweets', json=new_tweet)
    assert response.status_code == 201


def test_create_tweet_unsuccessful(client):
    invalid_tweet = {'text': 'Incomplete tweet data.'}
    response = client.post('/tweets', json=invalid_tweet)
    assert response.status_code == 400

