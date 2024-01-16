#!/usr/bin/python3
"""Function that queries the Reddit API and returns the number of subscribers"""
import requests

def number_of_subscribers(subreddit):
    """querying reddit api"""
    url = f"https://www.reddit.com/r/{subreddit}"
    header = {'User-Agent': 'CustomUserAgent'}
    res = requests.get(url, headers=headers)
    data = res.json()
    print(data['data'])
