#!/usr/bin/python3
"""
A function that querries the Reddit API and prints the
titles of the first 10 hot posts"""

import requests


def top_ten(subreddit):
    """Queries API returns 10 hot posts """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
            'User-Agent': 'Google Chrome Version 120.0.6099.217'
            }
    params = {
            'limit': 10
            }

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return
    output = response.json()
    hotPosts = output['data']['children']
    if len(hotPosts) == 0:
        print(None)
    else:
        for post in hotPosts:
            print(post['data']['title'])
