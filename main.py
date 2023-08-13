import tweepy
import keys_test

def get_api():
    auth = tweepy.OAuth1UserHandler(keys_test.api_keys, keys_test.api_secret)
    auth.set_access_token(keys_test.access_token, keys_test.access_token_secret)
    return tweepy.API(auth)

def tweet(api: tweepy.API, message: str, image_path=None):
    if image_path:
        api.update_with_media(image_path, status=message)
    else:
        api.update_status(message)

print('Tweeted successfully!')

if __name__ == '__main__':
    api = get_api()
    tweet(api, 'This was tweeted from python', 'cat.png')







 
