#!/usr/bin/python3
"""Function that queries the Reddit API and returns the number
of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """querying reddit api"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'CustomUserAgent'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        response = response.json()
        return response['data']['subscribers']
    else:
        return 0
