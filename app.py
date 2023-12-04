
from flask import Flask, jsonify, request
import json

app = Flask(__name__)


with open('100tweets.json', 'r') as file:
    tweets_data = json.load(file)


@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/tweets', methods=['GET'])
def get_all_tweets():
    return jsonify(tweets_data)

@app.route('/tweets_filtered', methods=['GET'])
def get_filtered_tweets():
    query_param = request.args.get('filter')
    if query_param:
        filtered_tweets = [tweet for tweet in tweets_data if query_param in tweet['text']]
        return jsonify(filtered_tweets)
    else:
        return jsonify(tweets_data)

@app.route('/tweet/<int:tweet_id>', methods=['GET'])
def get_tweet_by_id(tweet_id):
    try:
        tweet = next(tweet for tweet in tweets_data if tweet['id'] == tweet_id)
        return jsonify(tweet)
    except StopIteration:
        return jsonify({'error': 'Tweet not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400



@app.route('/tweets', methods=['POST'])
def create_tweet():
    try:
        new_tweet = request.get_json()

        if 'id' not in new_tweet or 'text' not in new_tweet:
            raise ValueError("Invalid tweet format. 'id' and 'text' are required.")

        tweets_data.append(new_tweet)
        return jsonify(new_tweet), 201  
    except ValueError as e:
        return jsonify({'error': str(e)}), 


if __name__ == '__main__':
    app.run(debug=True)
