#!/usr/bin/python3
"""Function that queries the Reddit API and returns the number
of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """querying reddit api"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Ubuntu 22.04.2 LTS'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        response = response.json()
        return response['data']['subscribers']
    else:
        return 0
