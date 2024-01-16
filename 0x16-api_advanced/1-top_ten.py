#!/usr/bin/python3
"""
The module querries the Reddit API to print the
titles of the first 10 hot posts"""
import requests


def top_ten(subreddit):
    """A function that queries API and returns 10 hot posts """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'CustomUserAgent'}

    response = requests.get(url, headers=headers,
                            allow_redirects=False)

    if response.status_code == 200:
        output = response.json()
        hotPosts = output['data']['children'][:10]
        if len(hotPosts) == 0:
            print(None)
        else:
            for post in hotPosts:
                print(post['data']['title'])
    else:
        print(None)
