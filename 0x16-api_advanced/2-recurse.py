#!/usr/bin/python3
"""This modeule has a function to query a list of all hot posts on a
given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns list of titles of all hot posts on a given subreddit
    subreddit (str):
            The subreddit to get the title
    hot_list (list):
            List of titles of given subreddit
    after:
        after value for pagination
    count:
        updates count based on no. of posts
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "Ubuntu 22.04.2 LTS"}
    params = {"after": after, "count": count, "limit": 100}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    # print(response.json().get("data"));
    if response.status_code == 200:
        results = response.json().get("data")
        after = results.get("after")
        count += results.get("dist")
        for c in results.get("children"):
            hot_list.append(c.get("data").get("title"))
        if after is not None:
            return recurse(subreddit, hot_list, after, count)
        return hot_list
