# coding: utf-8

import tweepy


consumer_key, consumer_secret, access_token, access_token_secret = 'BfHofrv3gmOOMBe04ip6wXi22', 'BsqlUapmXyq9t10ebaKtWQTox2P6FhrRCJq9N0SWrzoNKISVO9', '2534651012-9wM0uW6gS4dz6jJ56COUmxqWNwxJDwyuzaBtR0z', '4tafMMlIBVQBkiIoWrP8vevFxRT1Ven0PNvGASedau9v7'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

statuses = []
for i in range(1, int(api.me().statuses_count/200)+2): statuses += api.user_timeline(screen_name='gd_ghost', since_id=i*200, count=200)

numbers = 